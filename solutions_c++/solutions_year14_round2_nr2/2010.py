#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <utility>
#define pii pair<int, int>
#define VI vector < int >
#define PB push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORD(i,a,b) for(i=a;i>b;i--)
typedef long long LL;
using namespace std;
int main()
{
	int i,j,k,n,t;
	cin>>t;
	int a,b,c;
	for(k=1;k<=t;k++)
	{
		long long int ans=0;
		cin>>a>>b>>c;
		for(i=0;i<a;i++)
		{	
			for(j=0;j<b;j++)
			{
//				cout<<i<<" "<<j<<" "<<(i&j)<<endl;
				if( (i&j)<c)
					ans++;
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}

