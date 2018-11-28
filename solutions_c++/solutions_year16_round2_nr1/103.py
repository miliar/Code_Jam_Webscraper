	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int C = 303;

string patterns[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int cnt[C];

string get(int x)
{
	string res;
	int mn = 1e9;
	for(char c : patterns[x])
		mn = min(mn, cnt[c]);
	for(char c : patterns[x])
		cnt[c] -= mn;
	while(mn--)
		res += char('0' + x);
	return res;
}

int main()
{
	int tests = in();
	for(int _t = 1; _t <= tests; _t++)
	{
		cout << "Case #" << _t << ": ";
		string s, res;
		cin >> s;
		for(char c : s)
			cnt[c]++;
		res += get(0);
		res += get(2);
		res += get(6);
		res += get(8);
		res += get(3);
		res += get(4);
		res += get(1);
		res += get(7);
		res += get(5);
		res += get(9);
		sort(res.begin(), res.end());
		cout << res << endl;
	}
}
