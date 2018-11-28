#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>
#include <set>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pii pair<int,int> 
#define pdd pair<double,double>
#define ll long long

#define PI 2*acos(0.0)
#define EPS 1e-9
#define INF 1000000000

using namespace std;

int T, maxShy;
char peopleConf[1010];

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %s", &maxShy, peopleConf);
		int ans = 0, curStand = 0;

		for(int i = 0; i <= maxShy; i++)
		{
			if(peopleConf[i] == '0') continue;

			if(i > curStand)
			{
				int additional = i - curStand;
				ans += additional;
				curStand += additional;
			}
			
			curStand += peopleConf[i] - '0';
		}

		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

