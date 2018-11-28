#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>
#include <cstdlib>
#include <ctime>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()

bool good(string &s, int R, int P, int S) {
	for(int i = 0; i < sz(s); i++) {
		if(s[i] == 'R') R--;
		if(s[i] == 'P') P--;
		if(s[i] == 'S') S--;
	}
	return (R == 0 && P == 0 && S == 0);
}

void mysort(string &str, int l, int r) {
	int N = r - l;
	if(N == 1) return;
	int mid = (l + r) / 2;
	mysort(str, l, mid);
	mysort(str, mid, r);
	int sign = 0;
	for(int i = 0; i < N / 2; i++) {
		if(str[l+i] < str[mid+i]) {
			sign = -1;
			break;
		}
		if(str[l+i] > str[mid+i]) {
			sign = 1;
			break;
		}
	}
	if(sign == 1) {
		for(int i = 0; i < N / 2; i++) {
			swap(str[l+i], str[mid+i]);
		}
	}
}

string tree(string cur, int cnt, int N) {
	if(cnt == N) return cur;
	string res = "";
	for(int i = 0; i < cnt; i++) {
		res += cur[i];
		if(cur[i] == 'P') {
			res += "R";
		}
		else if(cur[i] == 'R') {
			res += "S";
		}
		else {
			res += "P";
		}
	}
	res = tree(res, cnt * 2, N);
	return res;
}

string check(int s, int N) {
	string x = "P";
	if(s == 1) x = "R";
	if(s == 2) x = "S";
	string res = tree(x, 1, N);
	return res;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		int R, P, S, N;
		scanf("%d", &N);
		N = 1 << N;
		scanf("%d %d %d", &R, &P, &S);
		string var0 = check(0, N);
		string var1 = check(1, N);
		string var2 = check(2, N);
		mysort(var0, 0, sz(var0));
		mysort(var1, 0, sz(var1));
		mysort(var2, 0, sz(var2));
		string IMPOSSIBLE = "IMPOSSIBLE";
		string res = "IMPOSSIBLE";
		if(good(var0, R, P, S) && (var0 < res || res == IMPOSSIBLE)) res = var0;
		if(good(var1, R, P, S) && (var1 < res || res == IMPOSSIBLE)) res = var1;
		if(good(var2, R, P, S) && (var2 < res || res == IMPOSSIBLE)) res = var2;
		cout << res << endl;
	}

	return 0;
}