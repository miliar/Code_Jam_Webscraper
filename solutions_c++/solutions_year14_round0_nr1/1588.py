#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <deque>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define B 33
#define MAX 100010
#define eps 1e-7
#define pi 3.14159
#define ull unsigned long long
#define MOD 1000000009

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int t;
int n;
int cnt[100];
int mat[100][100];

int main(void)
{
	cin >> t;
	
	int cases = 0;

	while(t--)
	{
		memset(cnt, 0, sizeof cnt);
		cin >> n;

		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 1 ; j <= 4; ++j)
			{
				cin >> mat[i][j];
			}
		}

		for (int i = 1; i <= 4; ++i)
		{
			cnt[mat[n][i]]++;
		}

		cin >> n;

		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 1 ; j <= 4; ++j)
			{
				cin >> mat[i][j];
			}
		}

		for (int i = 1; i <= 4; ++i)
		{
			cnt[mat[n][i]]++;
		}

		cout << "Case #" << ++cases << ": ";

		int cnt2 = 0;
		int idx;
		for (int i = 0; i <= 20; ++i)
		{
			if(cnt[i] == 2)
				cnt2++, idx = i;
		}

		if (cnt2 == 1)
		{
			cout << idx << "\n";
		}
		else if (cnt2 == 0)
		{
			cout << "Volunteer cheated!" << "\n";
		}
		else
			cout << "Bad magician!" << "\n";
	}
	return 0;
}