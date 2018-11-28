#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i,a,b)  for(__typeof(b) i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FOREACH(x,c)   for(__typeof(c.begin()) x=c.begin();x != c.end(); x++)
#define ALL(c)      c.begin(),c.end()
#define CLEAR(c)    memset(c,0,sizeof(c))
#define SIZE(c) (int) ((c).size())

#define PB          push_back
#define MP          make_pair
#define X           first
#define Y           second

#define ULL         unsigned long long
#define LL          long long
#define LD          long double
#define II         pair<int, int>
#define DD         pair<double, double>

#define VI          vector<int>
#define VVI         vector<VI >
#define VD                      vector<double>
#define VS          vector<string >
#define VII        vector<II >
#define VDD         vector< DD >

#define DUMP(a)       cerr << #a << ": " << a << endl;
using namespace std;

int tests;
LL n,p;
LL result1, result2;

vector<string> dict;

void read_test(){
	cin >> n >> p;
}

void can_win(){
	int needs_to_win=0;
	LL pp = p-1;
	REP(i,n){
		int win = 1-(pp%2);
		pp /= 2;
		if (win == 1){
			needs_to_win++;
		} else{
			if (needs_to_win > 1)
				needs_to_win = 1;
		}
	}
	LL bal = 0; // beats at least
	REP(i,needs_to_win)
		bal = 2*bal+1;
	result2 = (1LL << n) - bal - 1;
}

void must_win(){
	if (p == (1LL << n)){
		result1 = (1LL << n)-1;
		return;	
	}
	VI win(n);
	LL pp = p;
	int loss_count = 0;
	int reset = -1;
	REP(i,n){
		win[n-1-i] = 1-(pp%2);
		loss_count += (1-win[n-1-i]);
		if ((loss_count != 0) && (win[n-1-i] == 1))
			reset = n-1-i;
		pp /= 2;
	}
	if (reset != -1){
		win[reset] = 0;
		for(int i=reset+1; i < n; i++)
			win[i] = 1;
	}
	LL bam = 0; // beats at most
	//cout << p << " ";
	//REP(i,n) cout << win[i]  << " ";
	//cout << endl;
	REP(i,n)
		if (win[i] == 0)
			bam = 2*bam;
		else
			bam = bam+(1LL << i);
	result1 = (1LL << n) - bam - 2;
}

void solve_test(){
	must_win();
	can_win();
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result1 << " " << result2 << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
