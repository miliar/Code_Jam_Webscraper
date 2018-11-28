#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

bool bad = 0;

int brute(vector<int> a) {
	vector<int> t = a;

	sort(t.begin(), t.end());

	int ans = INF;

	vector<int> temp = a;

	vector<int> best_at;

	do {

		int at = 0;
		while (at + 1 < t.size() && t[at] < t[at + 1]) ++at;
		while (at + 1 < t.size() && t[at] > t[at + 1]) ++at;
		if (at == t.size() - 1) {
			int cur = 0;
			for (int to = 0; to < t.size(); ++to) {
				int z = 0;
				for (z = 0; z < a.size(); ++z) if (a[z] == t[to]) break;

				while(z != to) {
					++cur;
					swap(a[z], a[z-1]);
					--z;
				}

				if (cur > ans) break;
			}

			if (cur < ans) {
				ans = cur;

				best_at = t;
			}

			a = temp;
		}

	} while(next_permutation(t.begin(), t.end()));

	if (bad) {	
		cerr << "[";
		for (int i = 0; i < a.size(); ++i) {
			cerr << best_at[i] << " ";
		}
		cerr <<"]" << endl;
	}

	return ans;
}


	const int N = 1e3 + 5;

int my(vector<int> a) {
	int n = a.size();

	if (n == 1) {
		return 0;
	}

	int max_at = max_element(a.begin(), a.end()) - a.begin();

	a.erase(a.begin() + max_at);

	vector<int> temp = a;

	int sort_pref[N];
	sort_pref[0] = 0;
	for (int i = 1; i < a.size(); ++i) {
		sort_pref[i] = sort_pref[i - 1];
		int at = i;
		while (at > 0 && a[at] < a[at - 1]) {
			swap(a[at], a[at-1]);
			++sort_pref[i];
			--at;
		}
	}
	a = temp;

	int sort_suff[N];
	sort_suff[a.size() - 1] = 0;
	for (int i = ((int)a.size()) - 2; i >= 0; --i) {
		sort_suff[i] = sort_suff[i + 1];
		int at = i;
		while (at + 1 < a.size() && a[at] < a[at + 1]) {
			swap(a[at], a[at+1]);
			++sort_suff[i];
			++at;
		}
	}

	a = temp;

	int ans = INF;

	int best_at = -1;

	for (int place_at = 0; place_at <= a.size(); ++place_at) {
		int cur = abs(place_at - max_at);
		if (place_at > 0) cur += sort_pref[place_at - 1];
		if (place_at < a.size()) cur += sort_suff[place_at]; 

		if (ans > cur) {
			ans = cur;
			best_at = place_at;
		}
		ans = min(ans, cur);
	}

	if (bad) {
		cerr << "[best at = " << best_at << "]" << endl;
	}

	return ans;
}

int another(vector<int> a) {
	
	vector<int> at(a.size());
	for (int i = 0; i < a.size(); ++i) {
		at[a[i]] = i;
	}

	int left = 0, right = a.size() - 1;

	int ans = 0;

	for (int w = 0; w < a.size(); ++w) {
		int x = at[w];

		if (abs(x - left) < abs(right - x)) {
			while (x != left) {
				swap(a[x], a[x-1]);
				++ans;
				at[a[x]] = x;
				at[a[x-1]] = x - 1;
				--x;
			}
			++left;
		} else {
			while (x != right) {
				swap(a[x], a[x+1]);
				++ans;
				at[a[x]] = x;
				at[a[x+1]] = x + 1;
				++x;
			}
			--right;
		}
	}

	return ans;
}

int main() {


   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);


   /*
   int iter = 0;
   for (int tst = 0; tst < 100000; ++tst) {
	   if (++iter == 100) {
		   cerr << tst << endl;
		   iter = 0;
	   }
	   int n = 8;
	   vector<int> a(n);
	   for (int i = 0; i < n; ++i) a[i] = i;
	   random_shuffle(a.begin(), a.end());

	   if (brute(a) != another(a)) {		   
		   cout << "ERR";
		   exit(0);
	   }
   }*/


	int T; cin >> T;

	for (int test = 1; test <= T; ++test) {
		
		int n; cin >> n;
		
		vector<int> a(n);
		for (int i = 0; i < n; ++i) cin >> a[i];

		vector<int> tp = a;
		sort(tp.begin(), tp.end());
		for (int i = 0; i < a.size(); ++i) {
			for (int j = 0; j < a.size(); ++j) {
				if (tp[i] == a[j]) {
					a[j] = i;
				}
			}
		}

		cout << "Case #" << test << ": " << another(a) << endl;
	}

	
    return 0;
}