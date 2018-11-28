#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <vector>
#include <math.h>

#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SIZE(v) ((int)(v).size())
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
typedef long long ll;
typedef std::pair<ll,ll> PII;
typedef std::vector<PII> VPII;
using namespace std;

void solve()
{
	int row;
	cin >> row;
	int a[4][4];
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> a[i][j];
		}
	}
	int row2;
	cin >> row2;
	int b[4][4];
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> b[i][j];
		}
	}
	int num = 0;
	vector<int> v;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (a[row - 1][i] == b[row2 - 1][j])	{
				num++;
				v.push_back(a[row - 1][i]);
			}
		}
	}
	if (num == 0)
	{
		cout << "Volunteer cheated!" << endl;
	}
	else if (num == 1)
	{
		cout << v[0] << endl;
	}
	else
	{
		cout << "Bad magician!" << endl;
	}

}



int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		//cout << "Case #" + i;
		//cout << ": ";
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
