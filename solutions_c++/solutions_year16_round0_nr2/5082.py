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
	int c;
	int t;
	int n;
};

//output data structure
struct outd{
	int cid;

	int N;
};



//calculate function
void calculate(ind& input, outd& output) {

	//if ( input.cid != 3) return;


	int n = input.t+1;

	//int c = input.c;

	bool g[n][n];

	for ( int i = 0 ; i < n; i++) {
		for ( int j = i+1 ; j < n ;j++) {

			//cout << i << " & " << j << " --------"<<endl;
			if (i != j) {
				int fp = input.n-1;
				int fp2 = 0;

				for (;fp >= 0 && ((i & (1<<fp)) == 0 ) == ((j & (1<< fp)) == 0); fp--);



				bool canreach = true;
				for (;fp >=0;fp--,fp2++) {
					if ( ((i & (1<<fp)) == 0) == ((j & (1<<fp2))== 0)){
						canreach = false;
						break;
					}
				}

				g[i][j] = canreach;
				g[j][i] = canreach;


			} else {
				g[i][j] = false;
				g[j][i] = false;
			}

			//cout << g[i][j] << ", ";
		}



		//cout << endl;
	}



	int d[n];
	bool ch[n];

	for ( int i = 0; i < n; i++) {
		d[i] = INT_MAX;
		ch[i] = false;
	}

	d[input.c] = 0;

	for ( int i = 0 ; i < n-1; i++) {
		int min = INT_MAX;
		int next;

		for (int k = 0; k < n; k++){
			if ( !ch[k] && d[k] <=min){
				min = d[k];
				next = k;
			}
		}
		ch[next] = true;

		for ( int j = 0 ; j < n ;j++) {

			if (!ch[j] && g[next][j] && d[next] != INT_MAX  && d[next]+1 < d[j]){
				d[j] = d[next] + 1;
			}


		}
	}

	output.N = d[input.t];
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

			string s;
			inf >> s;

			//std::getline(inf, s);


			int val = 0;
			int target = 0;
			int k =0;
			for (; k < s.length(); k++) {

				char ch = s.c_str()[k];
				if (ch == '+') {
					val = val | (1 << k);
				} else if ( ch != '-') {
					i--;
					break;
				}

				target = target | (1<<k);
			}

			inval.c = val;
			inval.t = target;
			inval.n = k;
			//cout <<s <<"("<<k<<"):" << inval.c <<"   ->  " <<  inval.t<<endl;
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


			outf << "Case #" << ov.cid << ": " << ov.N << endl;




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
