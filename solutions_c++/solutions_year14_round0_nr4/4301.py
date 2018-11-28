#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <bitset>
#include <set>
#include <vector>
#include <cmath>
#include <stack>
#include <list>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define MAXN 101
#define LSONE(s) ((s)&(-s)) //LASTBIT


int main()
{
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		int n;
		scanf("%d",&n);
		double v1[n],v2[n];
		int r1 = 0, r2 = 0;
		
		for(int i=0;i<n;++i)
		{
			scanf("%lf",v1+i);
		}
		for(int i=0;i<n;++i)
		{
			scanf("%lf",v2+i);
		}
		
		sort(v2,v2+n);
		
		
		bool used[n];
		memset(used,false,sizeof used);
		
		for(int i=0;i<n;++i)
		{
			int j = 0;
			while( j<n )
			{
				if( v1[i] < v2[j] && used[j] == false )
				{
					used[j] = true;
					break;
				}
				j++;
			} 
			if( j < n )
			{
				r1++;
			}
			else
			{
				j = 0;
				while( used[j] == true ) j++;
				used[j] = true;
			}
		}
		
		sort(v1,v1+n);
		int j = n-1;
		
		for(int i=n-1;i>=0 && j>=0;--i)
		{
			while( j>=0 && v1[i] < v2[j] )
			{
				j--;
			}		
			if( j >= 0 )
			{
				j--;
				r2++;
			}	
		}
		printf("Case #%d: %d %d\n",t,r2,n-r1);
	}		
	return 0;
}
