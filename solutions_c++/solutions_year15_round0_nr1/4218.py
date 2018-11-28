#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

//#define SMALL
#define LARGE

int main()
{

	#ifdef SMALL
		freopen("A-small-attempt0.in","rt",stdin);
		freopen("A-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		int standing=0,ans=0,n,y;
		char x[1005];
		cin>>n>>x;
		for(int j = 0; j <= n; j++)
		{
			y = (int)x[j] - 48;
			if(j > standing)
			{
				ans = ans + j - standing;
				standing = standing + j - standing;
			}
			standing += y;
		}	
		
		cout<<"Case #"<<i<<": "<<ans<<endl;		
	}
	
	return 0;
}
