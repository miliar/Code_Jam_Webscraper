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
	int n;
	int j;
};

struct jamcoin{
	string coin;
	int divisors[9];
};

//output data structure
struct outd{
	int cid;

	list<jamcoin> coins;
};

//map<int, int[]> distances;

int primes[] =  {2,3,5,	7,	11,	13,	17,	19,	23,
29,	31,	37,	41,	43,	47,	53,	59,	61,	67,
71	,73,	79,	83,	89,	97,	101,	103,	107,	109,
113,	127,	131,	137,	139,	149,	151,	157,	163,	167,
173,	179,	181,	191,	193,	197,	199,	211,	223,	227,
229,	233,	239,	241,	251, 257,	263,	269,	271,	277,
281,	283,	293,	307,	311,	313,	317,	331,	337,	347,
349,	353,	359,	367,	373,	379, 383,	389,	397,	401,
409,	419,	421,	431,	433,	439,	443,	449,	457,	461,
463,	467,	479,	487,	491,	499,	503,	509,	521,	523,
541,	547,	557,	563,	569,	571,	577,	587,	593,	599,
601,	607,	613,	617,	619,	631,	641,	643,	647,	653,
659,	661,	673,	677,	683,	691,	701,	709,	719,	727,
733,	739,	743,	751,	757,	761,	769,	773,	787,	797,
809,	811,	821,	823,	827,	829,	839,	853,	857,	859,
863,	877,	881,	883,	887,	907,	911,	919,	929,	937,
941,	947,	953,	967,	971,	977,	983,	991,	997};

int primecount = 168;


//calculate function
void calculate(ind& input, outd& output) {


	//long bv = (long)pow(2.0,(input.n-1)) + 1;

	long bv = 2;

	for ( int i = 0; i < input.n-2; i++) {
		bv = bv * 2;
	}

	bv++;

	while (output.coins.size()  < input.j){
		bitset<32> bs(bv);
		string bstr= bs.to_string();
		cout << "bstr = "<<bstr<< ", bv = " << bv<< " for input" << input.n<< endl;
		jamcoin ji;
		ji.coin = bstr.substr(bstr.length() - input.n);
		bool foundForAll = true;
		for ( int base = 2; base <=10; base++) {
			long nrep = stol(bstr,nullptr, base);
			cout << nrep << " for base " << base<<  endl;
			bool found = false;
			for ( int i = 0 ; i < primecount ; i++ ){

				if (primes[i] < nrep && nrep % primes[i] == 0) {
					ji.divisors[base -2] = primes[i];
					cout << "    divisor = " << primes[i] <<endl;
					found = true;
					break;
				}
			}

			if (!found ) {
				foundForAll = false;
				break;
			}
		}

		if (foundForAll) {
			output.coins.push_back(ji);
		}

		bv+=2;
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

			inf >> inval.n;
			inf >> inval.j;


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


			outf << "Case #" << ov.cid <<":"<< endl;
			for (list<jamcoin>::iterator it  = ov.coins.begin(); it != ov.coins.end() ; it ++ ) {
				outf << it->coin;
				for ( int i = 0; i <9; i++) {
					outf << " " << it->divisors[i];
				}
				outf << endl;
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
