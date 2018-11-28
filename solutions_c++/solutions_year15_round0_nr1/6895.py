#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>
#include <cstring>
#include <set>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define all(v) ((v).begin, (v).end)
#define pb push_back
#define x first
#define y second
#define mp make_pair

using namespace std;

typedef pair<int,int> par;

typedef long long int tint;

int rank(char c)
{
	int a = (int) (c - '0');

	return (a);
}

bool check(int f, int s, string shy)
{
	int stand = rank(shy[0]) + f;
	int cur = 1;
	bool ok = (stand > 0);

	while(ok and (cur < s))
	{
		int cant = rank(shy[cur]);
		if(cur <= stand)
		{
			stand += cant;
		}
		else
		{
			ok = false;
		}
		cur++;
	}

	return (ok);
}

int main()
{
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,s;
	string shy;

	cin >> t;

	forn(caso,t)
	{
		cin >> s;
		cin >> shy;
		s++;
		int ans = 0;
		
		// busqueda lineal

		if(!check(0,s,shy))
		{
			// no puedo con low, puedo con hi
			int low = 0;
			int hi = s;
			int mid;

			while(hi - low > 1)
			{
				mid = (hi + low)/2;

				if(check(mid, s, shy)) hi = mid;
				else low = mid;
			}

			ans = hi;
		}

		cout << "Case #" << (caso+1) << ": " << ans << endl;
	}

	return 0;
}