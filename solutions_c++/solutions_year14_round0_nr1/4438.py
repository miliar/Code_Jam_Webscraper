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

int cnt[16];

int main()
{
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		int p1,p2;
		
		int x;
		
		set<int>x1;
		vector<int>v;
		
		scanf("%d",&p1);
		
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				scanf("%d",&x);
				if( i+1 == p1 )
				{
					x1.insert(x);
					v.pb(x);
				}
			}
		}
		
		scanf("%d",&p2);
		
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				scanf("%d",&x);
				
				if( i+1 == p2 )
				{
					x1.insert(x);							
					v.pb(x);
				}
			}
		}
		
		printf("Case #%d: ",t);
		if( x1.size() == 8 ) printf("Volunteer cheated!");
		else if( x1.size()==7 ) 
		{
			sort(v.begin(),v.end());
			for(int i=1;i<8;++i)
			{
				if( v[i] == v[i-1] ) { printf("%d",v[i]); break; }
			}			
		}
		else printf("Bad magician!");
		
		if( tt!=t ) printf("\n");
	}	
	return 0;
}
