#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <cstdio>
#include <functional>

using namespace std;

template<class T>
string tostring(T a){ stringstream ss; ss << a; return ss.str(); }

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> II;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])


void ins_all_prefs(set<string> &se, string s){
	stringstream ss;
	for(char c : s){
		se.insert(ss.str());
		ss << c;
	}
	se.insert(ss.str());
}

int main(){
	ifstream be("D-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int m, n;  be >> m >> n;
		vector<string> strs(m);
		FOR(i, m){
			be >> strs[i];
		}

		int ma = -1;
		int sol2 = -2;
		VI as(m);
		while(1){
			vector<set<string> > tries(n);
			FOR(i, m){
				ins_all_prefs(tries[as[i]], strs[i]);
			}
			int tot = 0;
			FOR(i, n){
				tot += SZ(tries[i]);
			}
			if(tot > ma){
				ma = tot;
				sol2 = 1;
			} else if(tot == ma){
				sol2++;
			}

			//inc:
			int i;
			for(i = 0; i < m && as[i] == n - 1; i++)
				as[i] = 0;
			if(i == m)
				break;
			as[i]++;
		}

		ki << "Case #" << tt + 1 << ": " << ma << " " << sol2 << endl; //modolas csak a nagyhoz kene
	}


	ki.close();
	return 0;
}