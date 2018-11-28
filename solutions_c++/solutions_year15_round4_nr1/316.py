#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

string s[200];
int cntr[200], cntc[200];

string solve() {
	int R, C;
	int ans = 0;
	cin >> R >> C;
	for (int i = 0; i < R; ++i ) { 
		cin >> s[i];
		//cout << s[i] << endl;
	}
	
	memset(cntr, 0, sizeof(cntr));
	memset(cntc, 0, sizeof(cntc));
	
	for (int i = 0; i < R; ++i ) {
		for (int j = 0; j < C; ++j ) {
			if (s[i][j] != '.') {
				++cntr[i];
				++cntc[j];
			} 
		}
	}
	
	for (int i = 0; i < R; ++i ) {
		for (int j = 0; j < C; ++j ) {
			if (s[i][j] != '.' && cntr[i]==1 && cntc[j]==1) 
				return "IMPOSSIBLE";
		}
	}

	for (int i = 0; i < R; ++i ) {
		vector<char> v;
		for (int j = 0; j < C; ++j ) {
			 if (s[i][j] != '.') v.push_back(s[i][j]);
		}
		if (v.size()==0) continue;
		if (v[0] == '<') ++ans;
		if (v[v.size()-1] == '>') ++ans;
	}
	
	
	for (int j = 0; j < C; ++j ) {
		vector<char> v;
		for (int i = 0; i < R; ++i ) {
			 if (s[i][j] != '.') v.push_back(s[i][j]);
		}
		if (v.size()==0) continue;
		if (v[0] == '^') ++ans;
		if (v[v.size()-1] == 'v') ++ans;
	}
	
	return to_string(ans);
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int caseNum;
	cin >> caseNum;
	for (int caseID = 1; caseID <= caseNum; ++caseID) {
		cout << "Case #" << caseID << ": " << solve() << endl;
		fflush(stdout);
	}
}