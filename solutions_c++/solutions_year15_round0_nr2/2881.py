#ifdef ONLINE_JUDGE
	#include <bits/stdc++.h>
#else
	#include <algorithm>
	#include <bitset>
	#include <cassert>
	#include <cmath>
	#include <cstdio>
	#include <cstdlib>
	#include <cstring>
	#include <iostream>
	#include <map>
	#include <set>
	#include <stack>
	#include <string>
	#include <utility>
	#include <vector>
	#include <queue>
#endif

using namespace std;

	// lambda : [] (int a, int b) -> bool { body return }
	// string r_str = R"(raw string)"

#define mp make_pair
#define mt make_tuple
#define eb emplace_back
#define pb push_back
#define LL long long
#define ULL unsigned long long
#define BASE 73
#define NMAX 10000
#define NMAX2 20001
#define MOD1 1000000007
#define ALL(V) (V).begin(), (V).end()
#define ALLR(V) (V).rbegin(), (V).rend()
#define CRLINE Duxar(__LINE__);
#define SHOWME(x) cerr << __LINE__ << ": " << #x << " = " << (x) << endl;
#define ENTER putchar('\n');

int dx4[] = {-1, 0, 1, 0};
int dy4[] = {0, 1, 0, -1};

int dx8[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy8[] = {0, 1, 1, 1, 0, -1, -1, -1};

void Duxar(int _this_line) {
#ifndef ONLINE_JUDGE
	printf("\n . . . . . . . . . . . . . Passed line - %d\n", _this_line);
#endif
}

template <class T>
void ReadNo(T &_value) {
	T _sign = 1;
	char ch;
	_value = 0;
	while(!isdigit(ch = getchar())) {
		(ch == '-') && (_sign = -1);
	}
	do {
		_value = _value * 10 + (ch - '0');
	} while(isdigit(ch = getchar()));
	_value *= _sign;
}

template <class T>
void AddNr(T &a, T b) {
	a = a + b;
	while (a >= MOD1) {
		a -= MOD1;
	}
	while (a < 0) {
		a += MOD1;
	}
}

int compute(int val) {
	if (val == 1) {
		return 0;
	}
	int ans = compute(val / 2);
	ans = ans * 2 + 1;
	if (val % 2 == 1) {
		++ans;
	}
	return ans;
}

void solve() {
	vector <int> values;
	int N, i, k, vmax = -1, ans, best = MOD1;
	
	ReadNo(N);
	values.resize(N);
	for (i = 0; i < N; ++i) {
		ReadNo(values[i]);
		vmax = max(values[i], vmax);
	}
	
	best = vmax;
	for (k = 1; k <= vmax; ++k) {
		ans = 0;
		for (i = 0; i < N; ++i) {
			if (values[i] > k) {
				if (values[i] % k > 0) {
					++ans;
				}
				ans += compute(values[i] / k);
			}
		}
		best = min(best, ans + k);
	}
	
	printf("%d\n", best);
	
}

int main(int nargs, char **args){

	if (nargs > 1) {
		freopen(args[1], "r", stdin);
	}
	else {
		freopen("input.cpp", "r", stdin);
	}
	
	int i, N;
	
	ReadNo(N);
	for (i = 1; i <= N; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}
