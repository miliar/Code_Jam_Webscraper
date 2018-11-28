#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;
const int markSize = 200000;
int ans;
bool mark[markSize];

void do_shift(string& s, int index) //inclusive
{
	reverse(s.begin(), s.begin() + index);
	for (int i = 0; i < index; ++i) {
		if (s[i] == '+') {
			s[i] = '-';
		} else {
			s[i] = '+';
		}
	}
}

int translate(const string& s)
{
	int p = 1;
	int num = 0;
	for (int i = 0; i < s.size(); ++i) {
		num += p * (s[i] == '+' ? 1 : 0);
		p *= 2;
	}
	return num;
}

long long translate_hash(const string& s)
{
	long long p = 1;
	long long num = 0;
	for (int i = 0; i < s.size(); ++i) {
		num += p * (s[i] == '+' ? 1 : 0);
		p *= 1997;
	}
	return num;
}

bool check(const string& s)
{
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}
void rec(string& s, int moves)
{
	if (moves > ans) {
		return;
	}
	if (check(s)) {
		ans = moves;
		return;
	}
	for (int i = s.size(); i>= 0; --i) {
		do_shift(s, i);
		int num = translate(s);
		if (mark[num] == false) {
			mark[num] = true;
			rec(s, moves + 1);
			mark[num] = false;
		}
		do_shift(s, i);
	}

}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int  k = 1; k <= t; ++k) {
		string s;
		cin >> s;
		for (int i = 0; i < markSize; ++i) {
			mark[i] = false;
		}

		ans = 10000000;
		//rec(s, 0);
		queue< pair<string, int> > q;
		q.push(make_pair(s, 0));
		while (!q.empty()) {
			string s  = q.front().first;
			int moves = q.front().second;
			q.pop();
			if (check(s)) {
				ans = moves;
				break;
			}
			for (int i = 0; i < s.size(); ++i) {
				do_shift(s, i + 1);
				int num = translate(s);
				if (mark[num] == false) {
					mark[num] = true;
					q.push(make_pair(s, moves + 1));
				}
				do_shift(s, i + 1);
			}
		}
		cout << "Case #" << k << ": "<< ans << endl;

	}
	return 0;
}