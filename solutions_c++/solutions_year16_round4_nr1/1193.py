#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 1024;
int const MAX_CH = 100100;

char st[MAX_CH];

int check(vector<char> qq) {
	while (qq.size() > 1) {
		vector<char> pp;
		int len = (int) qq.size();
		for (int i=0; i<len; i+=2) {
			char a = qq[i];
			char b = qq[i+1];

			if (a == b) return 0;

			if (a == 'R' && b == 'S')
				pp.push_back('R');
			else if (a == 'S' && b == 'R')
				pp.push_back('R');
			else if (a == 'S' && b == 'P')
				pp.push_back('S');
			else if (a == 'P' && b == 'S')
				pp.push_back('S');
			else if (a == 'P' && b == 'R')
				pp.push_back('P');
			else if (a == 'R' && b == 'P')
				pp.push_back('P');
		}
		qq = pp;
	}
	return 1;
}

string solve_slow(int N, int P, int R, int S) {
	vector<char> qq;
	for (int i=0; i<P; i++) qq.push_back('P');
	for (int i=0; i<R; i++) qq.push_back('R');
	for (int i=0; i<S; i++) qq.push_back('S');

	if (check(qq)) {
		string ans = "";
		for (int i=0; i<qq.size(); i++) ans += qq[i];
		return ans;
	}

	string mn = "";
	for (int i=0; i<qq.size(); i++) mn += (char) 'Z';

	while (next_permutation(qq.begin(),qq.end()))
		if (check(qq)) {
			string ans = "";
			for (int i=0; i<qq.size(); i++) ans += qq[i];
			mn = min(mn, ans);
		}

	if (mn[0]== 'Z') {
		return "IMPOSSIBLE";
	}
	return mn;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		cerr<<"\r"<<qqq<<"     ";
		printf("Case #%d:",qqq);

		//
		int N;
		int R,P,S;
		cin>>N>>R>>P>>S;

		cout<<" "<<solve_slow(N,P,R,S);
		//

		printf("\n");
	}
	return 0;
}