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

const long double EPS = 1e-6;

int solve(vector< vector< int > > sentences) {
	int need_n = sentences.size() - 2;

	int sz = 0;
	for (int i = 0; i < sentences.size(); ++i) {
		int cmax = *max_element(sentences[i].begin(), sentences[i].end());
		sz = max(sz, cmax);
	}
	++sz;

	int ans = 1e9;

	vector<int> is_first(sz, 0);
	vector<int> is_second(sz, 0);
	for (int i = 0; i < sentences[0].size(); ++i) {
		is_first[sentences[0][i]] = 1;
	}
	for (int i = 0; i < sentences[1].size(); ++i) {
		is_second[sentences[1][i]] = 1;
	}

	if (need_n == 0) {
		ans = 0;
		for (int i = 0; i < is_first.size(); ++i) {
			ans += is_first[i] * is_second[i];
		}
	}


	vector<int> cfirst;
	vector<int> csecond;
	for (int mask = 0; mask < (1 << need_n); ++mask) {
		cfirst = is_first;
		csecond = is_second;

		for (int i = 2; i < sentences.size(); ++i) {
			bool first = ((mask & (1 << (i-2))) != 0);
			
			for (int  z = 0; z < sentences[i].size(); ++z) {
				if (first) {
					cfirst[sentences[i][z]] = 1;
				} else {
					csecond[sentences[i][z]] = 1;
				}
			}
		}

		int cans = 0;
		for (int i = 0; i < cfirst.size(); ++i) {
			cans += cfirst[i] * csecond[i];
		}

		if (ans > cans) {
			ans = cans;
		}
	}

	return ans;
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#else
	#define taskname "cutting"
		//freopen(taskname".in","r",stdin);
		//freopen(taskname".out","w",stdout);
	#endif



	int tests_; cin >> tests_;
	for (int test_ = 1; test_ <= tests_; ++test_) {
		
		map<string, int> ids;
		int n; cin >> n;
		scanf(" \n ");

		vector< vector<int> > sentences;

		for (int i = 0; i < n; ++i) {
			string line;
			getline(cin, line);

			stringstream ss(line);
			string word;

			vector<int> sentence;

			while (ss >> word) {
				int id = ids.size();
				if (ids.count(word)) {
					id = ids[word];
				}

				ids[word] = id;

				sentence.push_back(id);
			}

			sentences.push_back(sentence);
		}


		int ans = solve(sentences);
		
		cout << "Case #" << test_ << ": " << ans << endl;		
		cerr << "Case #" << test_ << ": " << ans << endl;		
		
	}

	return 0;
}