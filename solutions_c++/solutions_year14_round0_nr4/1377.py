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
#define MAX 1010
#define eps 1e-7
#define pi 3.14159
#define ull unsigned long long
#define MOD 1000000009

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int t,n;
long double naom[MAX]; // cheater
long double ken[MAX];

int main(void)
{
	cin >> t;
	
	int cases = 0;

	while (t--)
	{
		cin >> n;

		int Dwar = 0; // D. war
		int war = 0; // normal war

		for (int i = 0 ; i < n; ++i)
		{
			cin >> naom[i];
		}

		for (int i = 0 ; i < n; ++i)
		{
			cin >> ken[i];
		}

		int is = 0;
		int ie = n-1;

		int j = n-1;

		sort(naom, naom + n);
		sort(ken, ken + n);

		while (is <= ie)
		{
			if (naom[ie] > ken[j])
			{
				Dwar++;
				ie--;
			}
			else
			{
				is++;
			}

			j--;
		}

		int i = 0;
		while (i < n)
		{
			int ok = 0;
			for (int j = 0; j < n; ++j)
			{
				if (ken[j] > naom[i])
				{
					ok = 1;
					ken[j] = -1;
					break;
				}
			}

			if (!ok)
			{
				war++;
			}
			i++;
		}

		cout << "Case #" << ++cases << ": ";

		cout << Dwar << " " << war << "\n";
	}
	return 0;
}