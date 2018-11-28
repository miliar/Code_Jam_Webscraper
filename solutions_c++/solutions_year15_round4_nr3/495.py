#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <deque>
#include <ctime>
#include <cstring>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

//#include <bits/stdc++.h>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

#define endl '\n'

#define forr(i, n) for(ll (i) = 0LL; (i) < (n); (i)++)
#define mp3(a, b, c) mp(a, mp(b, c))

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;
typedef vector < pll > vll;

int INT_MAX_VAL = (int)  0x3F3F3F3F;
int INT_MIN_VAL = (int) -0x3F3F3F3F;
ll LONG_MAX_VAL = (ll)   0x3F3F3F3F3F3F3F3F;
ll LONG_MIN_VAL = (ll)  -0x3F3F3F3F3F3F3F3F;

#define MAXN 500006
#define MOD 1000000007

unordered_map<string, int> wm;

vector<int> read_words()
{
	string sent;
	getline(cin, sent);
	stringstream ss;

	ss << sent;

	vector<int> words;
	string w;
	while(ss >> w) {
		int ind;
		if(wm.find(w) == wm.end()) {
			ind = wm.size();
			wm[w] = ind;
		} else {
			ind = wm[w];
		}

		words.push_back(ind);
	}
	return words;
}

void solve(int test)
{
	wm.clear();
	cout << "Case #" << test << ": ";

	ll n; cin >> n; cin.ignore();
	string en, fr, unk;
	string w;


	auto ven = read_words();
	auto vfr = read_words();
	vector<vector <int> > words(n - 2);
	forr(i, n - 2) 	words[i] = read_words();

	int res = INT_MAX_VAL;

	vector<int> eng_cnt(wm.size());
	vector<int> fre_cnt(wm.size());

	
	vector<int> eng_true(wm.size());
	vector<int> fre_true(wm.size());

	for(auto &i : ven) {
		++eng_true[i];
	}

	for(auto &i : vfr) {
		++fre_true[i];
	}

	for(int mask = 0; mask < (1 << (n - 2)); ++mask) {
		eng_cnt.assign(eng_cnt.size(), 0);
		fre_cnt.assign(fre_cnt.size(), 0);

		for(int i = 0; i < n - 2; ++i) {
			for(auto &s : words[i]) {
				if(mask & (1 << i)) {
					++eng_cnt[s];
				} else {
					++fre_cnt[s];
				}
			}
		}

		int cres = 0;
		for(int i = 0; i < eng_cnt.size(); ++i) {
			if(eng_cnt[i] + eng_true[i] > 0 && fre_cnt[i] + fre_true[i] > 0) {
				++cres;
			}
		}

		res = min(res, cres);
	}

	cout << res << endl;
//	cout << endl;
}

int main()
{
//	cin.tie(0);
//	ios::sync_with_stdio(false);

	int t; cin >> t;
	for(int i = 1; i <= t; ++i) solve(i);



	return 0;
}
