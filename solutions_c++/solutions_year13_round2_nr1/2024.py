#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;

#define REP(i,n) for (int i=0; i<n; i++)

void culc(int A, vector <int> &mote, int j, int count, vector <int> &result){
//	cout << "A:"<<A<<" j:"<<j<<" count:"<<count <<" mote:"<< mote[j]<< endl;
	if(j<mote.size()){
		if(A > mote[j]){
			culc(A+mote[j], mote, j+1, count, result);	//add
		}else{
//			cout << "A:" << A << " remove "<< count + mote.size()-j << endl;
	//			culc(A, mote, j+1, count+1, result);	//remove (skip)
			result.push_back(count+mote.size()-j);
			if(j+1 >= mote.size()){
				count++;
			}else{
				cout << "A:" << A << " add "<< endl ;
				culc(2*A-1, mote, j, count+1, result);	//add
			}
		}
	}else{
		result.push_back(count);
//		cout << "end" << endl;
	}
}

int main(int argc, char *argv[]){
	int testcase=0;	//Nth test
	int X;	//testcase
	cout << "input file: " << argv[1] << endl;
	ifstream inputfile(argv[1]);
	ofstream outputfile("output.txt");
	
	inputfile >> X;
	
	REP(i,X){
		int count=0;
		testcase++;
		int A,N;
		inputfile >> A >> N;
//		cout << "A:" << A <<" N:" <<N<<endl;
		
		vector<int> mote(N);
		REP(i,N){
			inputfile >> mote[i];
		}
		sort(mote.begin(),mote.end());
		REP(i,N){
//			cout << "mote[" << i << "]:" << mote[i] << endl;
			
		}
		int j=0;
		vector<int> result;
		
		if(A == 1){
			count = N;
		}else{
			culc(A, mote, j, count, result);
			count = result[0];
			REP(k,result.size()){
				if(count > result[k]) count = result[k];
			}
		}
		
		cout << "Case #" << testcase << ": " << count << endl;
		outputfile << "Case #" << testcase << ": " << count << endl;
	}
	return 0;
}
