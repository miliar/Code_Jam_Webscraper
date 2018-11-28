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

#include <bitset>


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
	int k;
	int c;
	int s;
};


//output data structure
struct outd{
	int cid;

	list<int> poss;
};


//calculate function
void calculate(ind& input, outd& output) {
	for ( int i =  0; i < input.k && i < input.s; i++) {
		output.poss.push_back(i+1);
	}
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

			inf >> inval.k;
			inf >> inval.c;
			inf >> inval.s;


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


			outf << "Case #" << ov.cid <<":";
			for (list<int>::iterator it  = ov.poss.begin(); it != ov.poss.end() ; it ++ ) {


					outf << " " << *it;

			}

			outf << endl;



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
			//cout<<"processing" << endl;

			ind& d = inputQueue.front();

			outd od;
			od.cid = d.cid;

			calculate(d, od);

			outputQueue.push(od);

			inputQueue.pop();
			outputcv.notify_one();
		} else {
			//cout<<"locking"<<endl;
			std::unique_lock<std::mutex> lk(inputm);
			inputcv.wait(lk, isInDataAvailable);
			// cout<<"released"<<endl;
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
