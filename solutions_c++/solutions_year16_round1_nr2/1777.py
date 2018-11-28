#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;


#define Max 10000000  

int n;
int a[100][100];
set< int > vc;
int num[100000];
void solve()
{
	set< int > ans;
	for (auto & it : vc) 
	//for( set< int > :: iterator it = vc.begin(); it != vc.end(); ++it )
	{
//		cout<<it<<" "<<num[it]<<endl;
		if( num[it] & 1)
		{
			ans.insert( it );
		}
	}


	for( auto & it : ans )
	{
		cout<<it<<" ";
	}
	cout<<endl;
}

int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		vc.clear();
		clr( num );
		cin>>n;
		for( int i = 0; i < (2*n)-1; ++i )
		{
			fr(j,0,n)
			{
				cin>>a[i][j];
				num[a[i][j]]++;
				vc.insert( a[i][j] );
			}
		}
		printf("Case #%d: ",c+1);
		solve();
	}
}
