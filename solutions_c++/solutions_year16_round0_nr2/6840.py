//https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <limits>
#include <sstream>
#include <typeinfo>
#include <bitset>

using namespace std;

#define MAX_S 100

typedef long long ll;
typedef bitset<MAX_S> pancake_t;

int max_blank(const pancake_t& p, int N = MAX_S)
{
	int ans = 0;
	for (int i = 0; i < N; i++)
		if (p.test(i))
			ans = i + 1;
	return ans;
}

string to_string(const pancake_t& p, int N = MAX_S)
{
	int N2 = max_blank(p, N);
	auto tmp = p.to_string('+', '-').substr(MAX_S - N2);
	reverse(tmp.begin(), tmp.end());
	string s;
	char prev = 0;
	for (auto c : tmp) {
		if (c != prev) {
			s += c;
			prev = c;
		}
	}
	return s;
}

pancake_t ctor(string S)
{
	int N = (int)S.length();
	reverse(S.begin(), S.end());
	return pancake_t(S.c_str(), S.length(), '+', '-');	//zero=+, one=-
}

void flip(pancake_t& p, int N)
{
	for (int i = 0; i < N; i++) {
		p.flip(i);
	}
	for (int i = 0; i < N / 2; i++) {
		auto tmp = p.test(i);
		p.set(i, p.test(N - i - 1));
		p.set(N - i - 1, tmp);
	}
}

map<string, ll> memo;

ll dfs(const pancake_t& p)
{
	if (p.none())
		return 0;
	auto key = to_string(p);
	//clog << key << endl;
	auto it = memo.find(key);
	if (it != memo.end())
		return it->second;
	auto& ret = memo[key];
	ret = numeric_limits<ll>::max()/2;
	int N = max_blank(p);
	for (int i = N; i > 0; i--) {
		auto p2 = p;
		flip(p2, i);
		ret = min(ret, dfs(p2)+1);
	}
	return ret;
}

ll solve(const string& S)
{
	return dfs(ctor(S));
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		auto ans = solve(S);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
