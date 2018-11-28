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
int n;
int result;
string text;

vector<string> dict;

void read_test(){
	cin >> text;
}

void read_dict(){
	fstream f("garbled_email_dictionary.txt");
	dict.resize(521196);
	REP(i,521196)
		f >> dict[i];
	f.close();
};

void solve_test(){
	int S = SIZE(text);
	result = S;
	vector<vector<int> > dyn(S+1,vector<int>(5,S));
	REP(j,5) dyn[0][j] = 0;
	REP(i,S+1){
		// try to append words at positions i+1,...,i+len
		for(int j=3; j >= 0; j--)
			dyn[i][j] = min(dyn[i][j],dyn[i][j+1]);
		REP(j,SIZE(dict)){
			string &s = dict[j];
			int L = SIZE(s);
			if (L > S-i)
				continue;
			else{
				int first_change = 100, last_change = -100, changes = 0;
				int ok = 1;
				REP(k,L)
					if (text[i+k] != s[k]){
						if (k-last_change < 5){
							ok = 0;		
							break;
						} else{
							changes++;
							first_change = min(first_change,k);
							last_change = k;
						}
					}
				if (!ok)
					continue;
				int cons = max(0,4-first_change);
				for(int k=cons; k <= 4; k++){	
					int new_k = min(4,min(L-last_change-1,k+L));
					dyn[i+L][new_k] = min(dyn[i+L][new_k], dyn[i][k]+changes);
				}
			}
		}	
	}
	result =  dyn[S][0];
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	read_dict();
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
