
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>
#include <map>
#include <queue>

using namespace std;

static int T,I,N;
static int P[26];
ifstream input;
ofstream output;

typedef unsigned long long ull;

struct Pair {
	char c;
	int num;
	Pair(char c, int num) : c(c), num(num) {

	}
};

struct comp {
bool operator() (const Pair& p1, const Pair& p2) {
	return p1.num < p2.num;
}
};


void solve() {

	int sum = 0;

	priority_queue<Pair, vector<Pair>,comp> q;
	for(int i=0;i<N;++i){
		Pair p('A'+i,P[i]);
		sum += P[i];
		q.push(p);
	}

/*	while(!q.empty()) {
		Pair p = q.top();q.pop();
		cout << p.c << ": " << p.num << endl;
	}
*/


	output << "Case #" << I << ":";

	if(sum%2!=0){
		Pair p = q.top();q.pop();
		output << " ";
		output << p.c;
		p.num--;
		if(p.num>0) {
			q.push(p);
		}
	}

	while(!q.empty()){
		Pair p = q.top();q.pop();
		output << " ";
		output << p.c;
		p.num--;
		if(p.num>0) {
			q.push(p);
		}

 		if(!q.empty()) {
     		Pair s = q.top();q.pop();
	    	output << s.c;
		    s.num--;
	    	if(s.num>0) {
		    	q.push(s);
    		}
		}



	}


	output << endl;
}



int main(){
	input.open("A-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(I=1;I<=T;++I){
		input >> N;
		cout << N << endl;

		for(int i=0;i<N;++i) {
			input >> P[i];
		}

		solve();
		//output << "Case #" << i << ": " << sol << endl;
	}


	input.close();
	output.close();


	return 0;
}




