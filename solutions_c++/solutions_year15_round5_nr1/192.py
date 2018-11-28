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

const int N = 1e6 + 500;
vector<int> g[N];

vector< pair<int, int> > ranges;

void dfs(int v, int path_min, int path_max, const vector<int>& s) {
	path_min = min(path_min, s[v]);
	path_max = max(path_max, s[v]);

	ranges[v] = make_pair(path_min, path_max);

	for (int i = 0; i < g[v].size(); ++i) {
		dfs(g[v][i], path_min, path_max, s);
	}
}

int solve_small(int n, int d, vector<int> s, vector<int> m) {
	for (int i = 0; i < n; ++i) g[i].clear();
	for (int i = 1; i < n; ++i) {
		g[m[i] % i].push_back(i);
	}
	ranges.clear();
	ranges.resize(n);

	dfs(0, 1e9, -1e9, s);


	int max_s = *max_element(s.begin(), s.end());
	int min_s = *min_element(s.begin(), s.end());

	int answer = 1;
	for (int start = -500; start <= 1500; ++start) {
		int c = 0;
		int end = start + d;
		if (ranges[0].first < start || ranges[0].second > end) continue;
		
		for (int i = 0; i < n; ++i) {
			if (start <= ranges[i].first && ranges[i].second <= end) {
				++c;
			}
		}

		answer = max(answer, c);
	}

	return answer;
}

struct Event {
	int at;
	bool start;

	Event () {}
	Event (int at, bool start) : at(at), start(start) {}
	bool operator < (const Event& other) const {
		if (at != other.at) return at < other.at;
		return start < other.start;
	}
};

int solve_big(int n, int d, vector<int> s, vector<int> m) {
	for (int i = 0; i < n; ++i) g[i].clear();
	for (int i = 1; i < n; ++i) {
		g[m[i] % i].push_back(i);
	}
	ranges.clear();
	ranges.resize(n);

	dfs(0, 1e9, -1e9, s);


	vector< pair<int, int> > cranges;

	vector< Event > events;

	for (int i = 0; i < n; ++i) {
		if (ranges[i].second - ranges[i].first <= d && ranges[0].first - d <= ranges[i].first && ranges[i].second <= ranges[0].second + d) {
			cranges.push_back(ranges[i]);
			events.push_back(Event(ranges[i].first, 1));
			events.push_back(Event(ranges[i].second, 0));
		}
	}

	sort(events.begin(), events.end());

	vector<int> through(3 * N, 0);

	int opened = 0;
	int p = 0;
	for (int at = 0; at < N; ++at) {
		while(p < events.size() && events[p].at == at) {
			if (events[p].start) ++opened;
			else --opened;
			++p;
		}
		through[at] = opened;
	}

	sort(cranges.begin(), cranges.end());

	int answer = 1;

	for (int start = s[0] - d; start <= s[0]; ++start) {
		int end = start + d;

		int range_start = lower_bound(cranges.begin(), cranges.end(), make_pair(start, 0)) - cranges.begin();
		int range_end = lower_bound(cranges.begin(), cranges.end(), make_pair(end + 1, 0)) - cranges.begin();

		int canswer = range_end - range_start - through[end];
		if (canswer > answer) {
			answer = canswer;
		}
	}

	return answer;
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
		
		int n, d;
		cin >> n >> d;
		long long s0, as, cs, rs;
		cin >> s0 >> as >> cs >> rs;
		long long m0, am, cm, rm;
		cin >> m0 >> am >> cm >> rm;

		vector<int> S(n), M(n);
		S[0] = s0;
		M[0] = m0;
		for (int i = 1; i < n; ++i) {
			S[i] = (as * S[i-1] + cs) % rs;
			M[i] = (am * M[i-1] + cm) % rm;
		}

		//int ans1 = solve_small(n, d, S, M);
		int ans = solve_big(n, d, S, M);
		//if (ans != ans1) {
		//	cerr << "ERR";
		//	exit(1);
		//} //else {
		//	cerr << "OK" << endl;
		//}

		cout << "Case #" << test_ << ": " << ans << endl;		
		cerr << "Case #" << test_ << ": " << ans << endl;
		//
		//cout << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;		
		//cerr << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}