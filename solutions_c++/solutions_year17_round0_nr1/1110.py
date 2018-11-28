#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

int const INT_INF = 1000000000;

char st[100100],ms[100100];
int K;

char next_ch(char x) {
	if (x == '-') return '+';
	if (x == '+') return '-';
	return 0;
}

int calc(char * s, int K, int fl) {
	string tt = s;
	if (fl) {
		tt = "";
		int n = (int) strlen(s);
		for (int i=n-1; i>=0; i--) tt += s[i];
	}

	if (K > (int) tt.length()) {
		for (int i=0; i<(int) tt.length(); i++)
			if (tt[i] == '-') return INT_INF;
		return 0;
	}

	int ans = 0;
	for (int i=0; i+K-1<(int) tt.length(); i++)
		if (tt[i] == '-') {
			ans++;
			for (int j=0; j<K; j++) tt[i+j] = next_ch(tt[i+j]);
		}

	for (int i=0; i<(int) tt.length(); i++)
		if (tt[i] == '-') return INT_INF;

	return ans;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int t;
	sscanf(st,"%d",&t);
	for (int q=1; q<=t; q++) {
		gets(st);
		sscanf(st,"%s %d",ms,&K);
		int cnt = 0;
		int ans = min(calc(ms,K,0), calc(ms,K,1));
		printf("Case #%d: ",q);
		if (ans >= INT_INF/2) printf("IMPOSSIBLE");
		else printf("%d",ans);
		printf("\n");
	}
	return 0;
}
