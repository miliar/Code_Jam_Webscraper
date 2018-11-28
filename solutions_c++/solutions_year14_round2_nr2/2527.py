#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define SMALL
//#define LARGE

int main()
{


	#ifdef SMALL
		freopen("B-small-attempt0.in","rt",stdin);
		freopen("B-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("B-large-attempt0.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		int j,l,a,b,k,ans;
		cin>>a>>b>>k;
		ans=a+b-1;
		for(j=1;j<a;j++)
		{
			for(l=1;l<b;l++)
			{
				if((j&l)<k)
					ans++;
			}
		}
			
		
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
	return 0;
}
