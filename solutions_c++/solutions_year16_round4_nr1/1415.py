#include<iostream>
#include<fstream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include<queue>
#include<set>
#include<cstring>
using namespace std;
typedef long long int ll;
typedef double lf;
typedef pair<int, int> pii;
const int INF = 2100000000;
const ll oo = 123456789987654321;
const ll MOD = 1000000007;

ifstream fin("input_a.txt");
ofstream fout("output_a.txt");

int TC;
int N, R, P, S;
bool ok;
int r, p, s;
string dfs(char x, int n) {
	if(n == N) {
		string tmp;
		tmp+=x;
		return tmp;
	}
	if(x == 'R') {
		if(dfs('R', n + 1) < dfs('S', n + 1)) {
			return dfs('R', n + 1) + dfs('S', n + 1);
		}
		else {
			return dfs('S', n + 1) + dfs('R', n + 1);
		}
	}
	if(x == 'S') {
		if(dfs('P', n + 1) < dfs('S', n + 1)) {
			return dfs('P', n + 1) + dfs('S', n + 1);
		}
		else {
			return dfs('S', n + 1) + dfs('P', n + 1);
		}
	}
	if(x == 'P') {
		if(dfs('P', n + 1) < dfs('R', n + 1)) {
			return dfs('P', n + 1) + dfs('R', n + 1);
		}
		else {
			return dfs('R', n + 1) + dfs('P', n + 1);
		}
	}
}
int main() {
	//scanf("%d", &TC)
	fin >> TC;
	for(int tc = 1; tc <= TC; tc++) {
		fin >> N >> R >> P >> S;
		ok = false;
		
		//printf("Case #%d: %d\n", ans);
		fout<<"Case #"<<tc<<": ";
		ok = false;
		string tmp = dfs('R', 0);
		p=s=r=0;
		for(int i = 0; i < tmp.size(); i++) {
			if(tmp[i] == 'P') p++;
			if(tmp[i] == 'S') s++;
			if(tmp[i] == 'R') r++;
		}
		if(p == P && r == R && s == S) {
			fout << tmp << endl;
			continue;
		}
		tmp = dfs('S', 0);
		p=s=r=0;
		for(int i = 0; i < tmp.size(); i++) {
			if(tmp[i] == 'P') p++;
			if(tmp[i] == 'S') s++;
			if(tmp[i] == 'R') r++;
		}
		if(p == P && r == R && s == S) {
			fout << tmp << endl;
			continue;
		}
		tmp = dfs('P', 0);
		p=s=r=0;
		for(int i = 0; i < tmp.size(); i++) {
			if(tmp[i] == 'P') p++;
			if(tmp[i] == 'S') s++;
			if(tmp[i] == 'R') r++;
		}
		if(p == P && r == R && s == S) {
			fout << tmp << endl;
			continue;
		}
		fout << "IMPOSSIBLE" << endl;
	}
}
