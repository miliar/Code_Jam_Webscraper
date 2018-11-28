//g++ -std=c++0x your_file.cpp -o your_program
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

string s, res;

inline void solve(int Case)
{
	printf("Case #%d: ", Case);
	cin >> s;
	res = "";
	res += s[0];
	for (int i = 1; i < (int)s.length(); i++)
	{
		if (s[i] >= res[0])
			res = s[i] + res;
		else
			res += s[i];
	}
	cout << res << endl;
}

int main()
{
	freopen (fname"input.txt", "r", stdin);
	freopen (fname"output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
		solve(i);
	return 0;
}
