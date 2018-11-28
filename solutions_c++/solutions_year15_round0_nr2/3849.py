#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <array>
#include <ctime>
#include <random>
#include <iomanip>

using namespace std;
typedef long long ll;

inline ll index(const array<int, 9>& a) {
	ll ans = 0;
	for (int i = 0; i < 9; ++i)
		ans = ans * 55 + a[i];
	return ans;
}
int simple(const vector<int>& p) {
	array<int, 9> cnt;
	cnt.assign(0);
	for (auto x : p)
		++cnt[x - 1];
	unordered_map<ll, int> h;
	queue<array<int, 9> > q;
	q.push(cnt);
	h[index(cnt)] = 0;
	while (!q.empty()) {
		array<int, 9> cur = q.front();
		int dist = h[index(cur)];
		q.pop();
		bool empty = true;
		for (int i = 9; i >= 1; --i)
			if (cur[i - 1]) {
				empty = false;
				for (int j = 1; j < i; ++j) {
					array<int, 9> mv = cur;
					--mv[i - 1];
					++mv[j - 1];
					++mv[i - j - 1];
					ll cur_ind = index(mv);
					if (h.find(cur_ind) == h.end()) {
						h[cur_ind] = dist + 1;
						q.push(mv);
					}
				}
			}
		if (empty)
			break;
		array<int, 9> mv = cur;
		for (int i = 1; i <= 8; ++i)
			mv[i - 1] = mv[i];
		mv[8] = 0;
		ll cur_ind = index(mv);
		if (h.find(cur_ind) == h.end()) {
			h[cur_ind] = dist + 1;
			q.push(mv);
		}
	}
	return h[0];
}
ostream& operator << (ostream& fout, const vector<int>& v) {
	for (auto& x : v)
		fout << x << " ";
	return fout;
}

void test() {
	auto beg = clock();
	default_random_engine gen(8439348);
	uniform_int_distribution<int> dist(1, 9);
	for (int q = 1; q <= 100; ++q) {
		vector<int> p(6);
		for (int& x : p)
			x = dist(gen);
		cout << "Test #" << q << ": " << p << " "<< simple(p) << "\n";
	}
	cout << fixed << setprecision(3) << "Done for " << (clock() - beg) * 1.0 / CLOCKS_PER_SEC;
}

void solve() {
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	auto beg = clock();
	fin >> t;
	for (int q = 0; q < t; ++q) {
		int d;
		fin >> d;
		vector<int> p(d);
		for (int i = 0; i < d; ++i)
			fin >> p[i];
		fout << "Case #" << q + 1 << ": " << simple(p) << "\n";
		cout << "Case #" << q + 1 << "\n";
	}
	cout << "Done for " << (clock() - beg) * 1.0 / CLOCKS_PER_SEC;
}

int main() {
	ios_base::sync_with_stdio(false);
	//test();
	solve();
	return 0;
}