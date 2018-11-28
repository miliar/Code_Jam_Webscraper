#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <ctime>

using namespace std;

#define ll long long
#define ld long double
#define sc second
#define fs first
#define mp make_pair

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;

const int N = 3e5 + 10, l = 20;

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

string _s[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int ord[] = { 6, 7, 5, 4, 0, 2, 8, 3, 1, 9 };
int _cnt[10][30];


void solve(int _case){
	string s;
	cin >> s;
	int cnt[30];
	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i < s.length(); i++)
		cnt[s[i] - 'A']++;

	vector<int> ans;
	for (int i = 0; i < 10; i++){
		int add = 10000;
		for (int j = 0; j < 27; j++){
			if (_cnt[ord[i]][j] == 0) continue;
			add = min(add, cnt[j] / _cnt[ord[i]][j]);
		}
		for (int j = 0; j < 27; j++){
			cnt[j] -= add*_cnt[ord[i]][j];
		}
		if (add == 10000) continue;
		while (add != 0){
			ans.push_back(ord[i]);
			add--;
		}
	}
	bool ok = 1;
	for (int i = 0; i < 30; i++)
		ok &= cnt[i] == 0;
	sort(ans.begin(), ans.end());
	cout << "Case #" << _case + 1 << ": ";
	for (auto i : ans)
		cout << i;
	if (!ok) cout << "LOL";
	cout << endl;
}

int main()
{
	FILE* f;
	freopen_s(&f, "input.in", "r", stdin);
	freopen_s(&f, "output.out", "w", stdout);
	for (int i = 0; i < 10; i++){
		for (int j = 0; j < _s[i].length(); j++)
			_cnt[i][_s[i][j] - 'A']++;
	}
	int t;
	cin >> t;
	for (int i = 0; i < t; i++){
		solve(i);
	}
	return 0;
}