#pragma comment(linker, "/STACK:512000000")
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

map< vector<int>, int > memo;
int brute(vector<int> p) {

	

	sort(p.rbegin(), p.rend());
	
	if (memo.count(p)) {
		return memo[p];
	}
	
	if (p.empty()) {
		return 0;
	}

	int& ans = memo[p];

	vector<int> t(p);
	for (int i = 0; i < t.size(); ++i) {
		--t[i];
	}
	while(!t.empty() && t.back() == 0) {
		t.pop_back();
	}

	ans = brute(t) + 1;

	for (int w = 0; w < p.size(); ++w) {
		vector<int> t(p);
		t.push_back(0);
		for (int left = 1; left < p[w]; ++left) {
			t[w] = left;
			t.back() = p[w] - left;

			ans = min(ans, brute(t) + 1);
		}
	}

	return ans;
}

int solve (vector<int> p) {
	sort(p.begin(), p.end());

	int answer = p.back();

	for (int remain = 1; remain <= p.back(); ++remain) {
		int extra = 0;
		for (int i = 0; i < p.size(); ++i) {
			extra += (p[i] + remain - 1) / remain - 1;
		}

		answer = min(answer, remain + extra);
	}

	return answer;
}

int main() {

	
	/*
	int t = 0;
	while (true) {
		vector<int> p;
		int n = rand() % 6 + 1;
		for (int i = 0; i < n; ++i) {
			p.push_back(rand() % 9 + 1);
			
		}

		if (solve(p) != brute(p)) {
			cerr << solve(p) << endl;
			cerr << brute(p) << endl;
			for (int i = 0; i < p.size(); ++i) {
				cerr << p[i] << " ";
			}
			exit(1);
		}

		++t;
		if (t % 1000 == 0) {
			cerr << t << ", " << memo.size() << endl;
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
		cin >> n;		
		vector<int> p(n);
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}

		int answer = solve(p);
		
		printf("Case #%d: %d\n", test, answer);
		eprintf("Case #%d: %d\n", test, answer);
	}




	return 0;
}