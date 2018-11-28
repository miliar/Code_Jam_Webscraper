//============================================================================
// Name        : codejam.cpp
// Author      : uditha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <thread>
#include <fstream>
#include <string>
#include <list>
#include <queue>


#include <sstream>>


#include <mutex>
#include <condition_variable>

using namespace std;

std::mutex inputm;
std::condition_variable inputcv;

std::mutex outputm;
std::condition_variable outputcv;


bool readFinished = false;
bool processFinished = false;


//input data structure
struct ind {
	int cid;
	unsigned long N;
};

//output data structure
struct outd{
	int cid;

	unsigned long nN;
};

//calculate function
void calculate(ind& input, outd& output) {
	unsigned long N = input.N;

	if ( N == 0 ) {
		output.nN = 0;
		output.cid = input.cid;
		return;
	}

	unsigned long nN =  0;

	int cd = 0;

	while (cd != 1023) {
		nN += N;
		ostringstream convert;
		convert << nN;
		string  s =  convert.str();

		for ( int i  = 0; i < s.length(); i++) {
			cd =  cd | 1 << (*(s.c_str() + i) - '0');
		}

		cout << N << ","<< nN << "===>" << cd <<endl;

	}

	output.nN = nN;
	output.cid = input.cid;

}

queue<ind> inputQueue;
queue<outd> outputQueue;





bool isInDataAvailable(){
	return !inputQueue.empty() || readFinished;
}

bool isOutDataAvailable(){
	return !outputQueue.empty() || processFinished;
}

//read input
void readInput()
{
	string line;
	ifstream inf ("./1.in");
	if (inf.is_open())
	{

		int T;//test cases;

		inf >> T;

		for ( int i = 1; i <= T; i++) {
			ind inval;
			inf >> inval.N;
			inval.cid = i;

			inputQueue.push(inval);

			inputcv.notify_one();

		}

		inf.close();
	}

	else cout << "Unable to open file";

	//cout<<"items:"<<inputQueue.size();

	readFinished = true;

	inputcv.notify_one();

}


//write output
void writeOutput()
{
	ofstream outf ("./1.out");
	while (!processFinished || !outputQueue.empty()){
		if (!outputQueue.empty()){
			//cout<<"writing" << endl;


			outd& ov = outputQueue.front();

			if ( ov.nN == 0) {
				outf << "Case #" << ov.cid << ": INSOMNIA" << endl;
			} else {
				outf << "Case #" << ov.cid << ": " << ov.nN << endl;
			}



			outputQueue.pop();
			outputcv.notify_one();
		} else {
			//cout<<"locking2"<<endl;
			std::unique_lock<std::mutex> lk(outputm);
			outputcv.wait(lk, isOutDataAvailable);
			 //cout<<"released2"<<endl;
		}
	}

	outf.close();
}

void process()
{
	while (!readFinished || !inputQueue.empty()){
		if (!inputQueue.empty()){
			cout<<"processing" << endl;

			ind& d = inputQueue.front();

			outd od;

			calculate(d, od);

			outputQueue.push(od);

			inputQueue.pop();
			outputcv.notify_one();
		} else {
			cout<<"locking"<<endl;
			 std::unique_lock<std::mutex> lk(inputm);
			 inputcv.wait(lk, isInDataAvailable);
			 cout<<"released"<<endl;
		}
	}

	processFinished = true;

	outputcv.notify_one();

	//cout<<"writebuf"<<outputQueue.size();
}




int main() {
	std::thread inputThread (readInput);
	std::thread outputThread (writeOutput);


	process();

	inputThread.join();
	outputThread.join();


	std::cout << "completed.\n";


	return 0;

}
