#include <iostream> 
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm> 
#include <cmath> 

#include <vector> 
#include <set>
#include <map>
#include <string>
#include <bitset>
#include <queue>
#include <unordered_map>
#include <sstream>


using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;
ll gcd(ll a, ll b)
{
	return b ? gcd(b, a%b) : a;
}

char beat(char c1, char c2)
{
	if (c1 == c2)
		return 'T';
	if (c1 == 'R')
		return (c2 == 'S') ? c1 : c2;
	if (c1 == 'S')
		return (c2 == 'R') ? c2 : c1;
	return (c2 == 'S') ? c2 : c1;
}

bool check(string cur)
{
	string cur2 = "";
	while (cur.size() != 1)
	{
		for (int i = 0; i < cur.size(); i += 2)
		{
			char rr = beat(cur[i], cur[i + 1]);
			if (rr == 'T')
				return 0;
			cur2 += rr;
		}
		cur = cur2;
		cur2 = "";
	}
	return 1;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		string res = "IMPOSSIBLE";
		int n, r, p ,s;
		cin >> n >> r >> p >> s;
		string cur = "";
		for (int i = 0; i < p; ++i)
			cur += 'P';
		for (int i = 0; i < r; ++i)
			cur += 'R';
		for (int i = 0; i < s; ++i)
			cur += 'S';
		bool fl = 1;
		while (fl)
		{
			//cout << cur << endl;
			if (check(cur))
			{
				res = cur;
				break;
			}
			fl = next_permutation(cur.begin(), cur.end());
		}
		printf("Case #%d: ", t);
		cout << res << '\n';
	}
	return 0;
}