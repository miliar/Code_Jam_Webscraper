#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <stack>
#include <map>
#include <numeric>
using namespace std;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define out(x) cout << (x) << endl;
#define fill(a, x) memset(a, x, sizeof(a))
#define all(c) c.begin(), c.end()
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
const int INF = (long long) 1e9;

pair <string, vi> compress(string s) {
	char last = s[0];
	string res; res += s[0];
	vi chain;
	int ctr = 0;
	for(int i = 0; i < s.size(); i++) {
		if (s[i] != last) {
			res += s[i];
			last = s[i];
			chain.pb(ctr);
			ctr = 1;
		} else {
			ctr++;
		}
	}
	chain.pb(ctr);
	return make_pair(res, chain);
}

int cost(string source, string target) {
	int ans = 0;
	vi source_chain = compress(source).Y;
	vi target_chain = compress(target).Y;
	for(int i = 0; i < source_chain.size(); i++)
		ans += abs(source_chain[i] - target_chain[i]);
	return ans;
}

int solve(vector<string> &strings) {
	string first = compress(strings[0]).X;
	int mincost = 0, curcost;
	for(int i = 0; i < strings.size(); i++)
		mincost += cost(strings[i], first);
	for(int i = 0; i < strings.size(); i++) {
		curcost = 0;
		for(int j = 0; j < strings.size(); j++) {
			curcost += cost(strings[i], strings[j]);
		}
		mincost = min(mincost, curcost);
	}
	return mincost;
}

int main() {
	int T;
	// string x = compress("mmaw").X;
	// out(x);
	// vi test = compress("mmaw").Y;
	// for(int i = 0; i < test.size(); i++)
	// 	out(test[i]);
	cin >> T;

	for(int t = 1; t <= T; t++) {
		int N, flag = 0;
		cin >> N;
		vector<string> strings(N, "");
		for(int i = 0; i < N; i++) 
			cin >> strings[i];
		
		string prev = compress(strings[0]).X;
		for(int i = 0; i < N; i++) {
			if (compress(strings[i]).X != prev) {
				flag = 1;
				break;
			}
		}
		if (flag) {
			printf("Case #%d: Fegla Won\n", t);
			continue;
		}
		int minmoves = solve(strings);
		printf("Case #%d: %d\n", t, minmoves);

	}
}

