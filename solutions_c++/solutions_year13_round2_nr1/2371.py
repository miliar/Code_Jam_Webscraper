/*
 * a.cpp
 *
 *  Created on: May 4, 2013
 *      Author: ock
 */
#include <fstream>
#include <queue>
#include <vector>

using namespace std;

class compare{
public:
	bool operator()(const int& a,const int& b){
		return a>b;
	}
};

ifstream scanner;
ofstream out;
int T;
int A;
int N;
priority_queue<int,vector<int>,compare >mote;
priority_queue<int,vector<int>,compare >empty;
int testcase;
vector<int> sorted_mote;

void sort(){
	sorted_mote.clear();
	for (int i = 0; i < N; ++i) {
		int a = mote.top(); mote.pop();
		sorted_mote.push_back(a);
	}
}


/*
void solve(){
	int numoperations = 0;
	while(!mote.empty()){
		int minmote = mote.top(); mote.pop();
		if(minmote<A){
			A+=minmote;
		}
		else if(2*A-1>minmote){
			A+=A-1+minmote;
			numoperations++;
		}
		else{
			numoperations++;
		}

	}

	out << "Case #" << testcase <<": " << numoperations << endl;
}*/


int solve1(int i,int Asize,int op){
	int minmote;
	while(i<N){
		minmote = sorted_mote[i];
		if(minmote<Asize){
			Asize+=minmote;
			i++;
		}
		else
			break;
	}

	if(i<N){
		int a;
		if(Asize!=1)
			a= solve1(i,2*Asize-1,op+1);
		else
			a=N;
		int b = solve1(i+1,Asize,op+1);


		if(a<b)
			return a;
		else
			return b;
	}
	else
		return op;
}

int solve1(){
	return solve1(0,A,0);
}

int main(){

	scanner.open("A-small-attempt2.in");
	//scanner.open("input.txt");
	out.open("output.txt");

	scanner >> T;

	for(int i=1;i<=T;i++){
		testcase=i;
		scanner >> A >> N;
		mote = empty;

		for (int j = 0; j < N; ++j) {
			int a;
			scanner >> a;
			mote.push(a);
		}
		sort();
		int f=solve1();
		out << "Case #" << testcase <<": " << f << endl;

	}

	scanner.close();
	out.close();



	return 0;
}


