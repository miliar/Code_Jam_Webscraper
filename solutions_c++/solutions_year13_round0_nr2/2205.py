#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

vector<vector <int> >mp,nmp;
int n, m;

string solve(){
	int mx;

	REP(i,n){
		mx = 0;
		REP(j,m) if(mp[i][j]>mx)mx = mp[i][j];
		REP(j,m) nmp[i][j] = min(mx, nmp[i][j]);
	}
	
	REP(i,m){
		mx = 0;
		REP(j,n) if(mp[j][i]>mx)mx = mp[j][i];
		REP(j,n) nmp[j][i] = min(mx, nmp[j][i]);
	}
	
	mx = 1;
	REP(i,n){
		REP(j, m){
			if(mp[i][j]!=nmp[i][j]){
				return "NO";
			}
		}
	}
	return "YES";
}

int main(void){
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	int ntest;
	

	fin >> ntest;

	REP(w, ntest){
		fin >> n >> m;
		mp.resize(n);
		nmp.resize(n);
		REP(i,n){
			mp[i].resize(m);
			nmp[i].resize(m);
			REP(q,m) {
				fin >> mp[i][q];
				nmp[i][q] = 100;
			}

		}
		fout << "Case #" << w+1 << ": " << solve() << endl;
	}


	fin.close();
	fout.close();
	return 0;
}