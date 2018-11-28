#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <string>
#include <sstream>
#include <math.h>
#include <stack>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

int brute(const string& s) {
	for (int have = 0; ; ++have) {
		int chave = have;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] != '0') {
				if (chave >= i) {
					chave += (s[i] - '0');
				} else {
					goto end;
				}
			}
		}
		return have;
		end:;
	}
}

int solve(const string& s) {
	int answer = 0;
	int have = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] != '0') {
			if (have >= i) {
				have += (s[i] - '0');
			} else {
				answer += i - have;
				have = i;
				have += (s[i] - '0');
			}
		}
	}

	return answer;
}

int main() {

	/*
	int t = 0;
	while (true) {
		string s;
		int n = rand() % 1000 + 1;
		for (int i = 0; i < n; ++i) {
			s += '0' + rand() % 10;
			
		}
		s += '1' + rand() % 9;

		if (solve(s) != brute(s)) {
			exit(1);
		}

		++t;
		if (t % 1000 == 0) {
			cerr << t << endl;
		}
	}
	*/
	
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#else
	#define taskname "cutting"
		//freopen(taskname".in","r",stdin);
		//freopen(taskname".out","w",stdout);
	#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n;
		string s;
		cin >> n >> s;

		int answer = solve(s);

		printf("Case #%d: %d\n", test, answer);
		eprintf("Case #%d: %d\n", test, answer);
	}




	return 0;
}