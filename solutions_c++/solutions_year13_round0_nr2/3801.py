#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

int barisMax[105];
int kolomMax[105];
int petak[105][105];

int
main()
{
	int T;
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		for(int i = 0;i < 105;i++)
		{
			barisMax[i] = -1;
			kolomMax[i] = -1;
		}

		int X,Y;
		scanf("%d %d", &X,&Y);
		for(int i = 0;i < X;i++)
		{
			for(int j = 0;j < Y;j++)
			{
				int tmp;
				scanf("%d", &tmp);
				petak[i][j] = tmp;
				barisMax[i] = max(barisMax[i],tmp);
				kolomMax[j] = max(kolomMax[j],tmp);
			}
		}
		bool yes = true;
		for(int i = 0;i < X && yes;i++)
		{
			for(int j = 0;j < Y && yes;j++)
			{
				if(petak[i][j] < barisMax[i] && petak[i][j] < kolomMax[j])
				{
					yes = false;
					break;
				}
			}
		}		
		printf("Case #%d: %s\n",tc,yes ? "YES" : "NO");
	}
return 0;
}