#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

int M,N;
vector<string> S;
vector<vector<string> > prefix;
set<vector<set<string> > > res;

void rec(int idx,vector<vector<string> > &combined){
	if (idx == M){
		vector<set<string> > result(N, set<string>());
		bool ok = true;
		REP(i, N){
			REP(j, combined[i].size())result[i].insert(combined[i][j]);
			if (result[i].size() == 0)ok = false;
		}
		//sort(ALL(result));
		if (ok)res.insert(result);
	}
	else{
		REP(i, N){
			combined[i].push_back(S[idx]);
			rec(idx + 1, combined);
			combined[i].pop_back();
		}

	}
}

int main(){
	int T;
	cin >> T;
	REP(testCase, T){
		cin >> M >> N;
		S.resize(M);
		prefix.assign(M, vector<string>());
		REP(i, M)cin >> S[i];

		REP(i, M){
			for (int j = 1; j <= (int)S[i].size(); j++){
				prefix[i].push_back(S[i].substr(0, j));
				//cout << S[i].substr(0, j) << " " ;
			}
			//cout << endl;
			//REP(j, prefix[i].size())cout << prefix[i][j] << " ";
			//cout << endl;
		}

		res.clear();
		vector<vector<string> > combined(M, vector<string>());
		rec(0,combined);
		int mxNode = 0;
		int way = 0;
		for (set<vector<set<string> > >::iterator it = res.begin(); it != res.end(); it++){
			int tmp = 0;
			REP(i, (*it).size()){
				set<string> pre;

				for (set<string>::iterator jt = (*it)[i].begin(); jt != (*it)[i].end(); jt++){
					string s = *jt;
					REP(j,s.size()+1)pre.insert(s.substr(0, j));
					//cout << (*jt) << " ";
				}
				tmp += pre.size();
				//cout << endl;
			}
			//cout << endl;
			if (tmp > mxNode){
				mxNode = tmp;
				way = 0;
			}
			if (mxNode == tmp)way++ ;
		}
		cout << "Case #" << testCase + 1 << ": " << mxNode << " " << way << endl;
	}
	return 0;
}