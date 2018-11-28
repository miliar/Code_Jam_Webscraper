//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
using namespace std;

int arr[10050];
bool udah[10050];

int main()
{
	int t;
	scanf("%d",&t);
	FORN(i,t)
	{
		int n,x;
		scanf("%d%d",&n,&x);
		FORN(j,n)
			scanf("%d",&arr[j]);
		sort(arr,arr+n);
		RES(udah,false);
		int ans = 0, z = n-1;
		while (z >= 0)
		{
			while ((z >= 0) && udah[z])
				z--;
			if (z < 0)
				break;
			udah[z] = true;
			ans++;
			int y = z-1;
			while ((y >= 0) && (arr[z]+arr[y] > x))
				y--;
			while ((y >= 0) && udah[y])
				y--;
			if (y < 0)
				continue;
			udah[y] = true;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}
