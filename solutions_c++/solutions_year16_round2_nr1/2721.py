#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>
#include<vector>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<iomanip>
#include <functional>
using namespace std;
typedef long long ll;
const int mod = 1000000007;
const int INF = 1 << 28;
//cout << fixed << std::setprecision(9)
//memset(a, 0, sizeof(a));
//--------------------------

int t;

string solve(string s)
{
	int num[26];
	int count[10];
	string ans;
	memset(num, 0, sizeof(num));
	memset(count, 0, sizeof(count));

	for (int i = 0; i < s.size(); i++) {
		num[s[i] - 'A']++;
	}

	while (num['Z' - 'A']) {
		count[0]++;
		num['Z' - 'A']--;
		num['E' - 'A']--;
		num['R' - 'A']--;
		num['O' - 'A']--;
	}

	while (num['X' - 'A']) {
		count[6]++;
		num['S' - 'A']--;
		num['I' - 'A']--;
		num['X' - 'A']--;
	}

	while (num['W' - 'A']) {
		count[2]++;
		num['T' - 'A']--;
		num['W' - 'A']--;
		num['O' - 'A']--;
	}

	while (num['S' - 'A']) {
		count[7]++;
		num['S' - 'A']--;
		num['E' - 'A']--;
		num['V' - 'A']--;
		num['E' - 'A']--;
		num['N' - 'A']--;
	}

	while (num['V' - 'A']) {
		count[5]++;
		num['F' - 'A']--;
		num['I' - 'A']--;
		num['V' - 'A']--;
		num['E' - 'A']--;
	}

	while (num['G' - 'A']) {
		count[8]++;
		num['E' - 'A']--;
		num['I' - 'A']--;
		num['G' - 'A']--;
		num['H' - 'A']--;
		num['T' - 'A']--;
	}

	while (num['F' - 'A']) {
		count[4]++;
		num['F' - 'A']--;
		num['O' - 'A']--;
		num['U' - 'A']--;
		num['R' - 'A']--;
	}

	while (num['O' - 'A']) {
		count[1]++;
		num['O' - 'A']--;
		num['N' - 'A']--;
		num['E' - 'A']--;
	}

	count[3] = num['R' - 'A'];
	count[9] = num['I' - 'A'];

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < count[i]; j++) {
			ans += ('0' + i);
		}
	}

	return ans;
}

int main()
{
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}

	return 0;
}