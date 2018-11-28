#include "stdafx.h"
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <fstream>
#include <iostream>
using namespace std;

#define INF 300000000
#define MOD 1000000007LL
#define COUT f
typedef long long ll;

int Q, N, M, K, L;

bool chk[11];

char r(char x) {
	return x == '+' ? '-' : '+';
}

int main() {
	ofstream f;
	f.open("result.txt");
	cin >> Q;
	for (int qq = 0; qq < Q; qq++) {
		string s;
		cin >> s;
		int size = s.size();
		int st = 0;
		int ret = 0;
		for (int i = 1; i < size; i++) {
			if (s[i] != s[st]) {
				char x = r(s[0]);
				for (int j = 0; j < i; j++) s[j] = x;
				st = i;
				ret++;
			}
		}
		if (s[0] == '-') ret++;
		COUT << "Case #" << qq + 1 << ": ";
		COUT << ret << "\n";
	}
	cin >> N;
}