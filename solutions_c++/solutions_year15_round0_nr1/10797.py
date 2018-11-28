#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>
#pragma comment(linker, "/STACK:16777216")

using namespace std;
 
 
#define sqr(a) (a)*(a)
#define mp make_pair


typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
const ld PI = acos(-1.0);
const ld EPS = 1e-12;
const int MAXN = (int)2e3;
const int INF = (int)1e9+7;




vector <int> m;
vector <string> p;
vector <int> ans;


bool check(int a, int b)
{
	for (int i = 0; i <= m[a]; ++i)
		if (b > 8) return true;
		else if (b >= i)
			b += p[a][i] - 48;
		else return false;
	return true;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin >> n;


	m.resize(n);
	p.resize(n);
	ans.resize(n);

	for (int i = 0; i < n; ++i)
	{
		cin >> m[i];
		getline(cin, p[i]);
		p[i] = p[i].substr(1, p[i].size());
	}



	for (int i = 0; i < n; ++i)
		for (int j = 0; j < 9; ++j)
			if (check(i, j))
			{
					ans[i] = j;
					break;
			}



	for (int i = 0; i < n; ++i)
		cout << "Case #" << i+1 << ": " << ans[i] << endl;

	return 0;
}