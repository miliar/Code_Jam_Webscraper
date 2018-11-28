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
		freopen("D-small-attempt0.in","rt",stdin);
		freopen("D-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("D-large.in","rt",stdin);
		freopen("D-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		int x,r,c,n;
		cin>>x>>r>>c;	
		n = r * c;
		if((n % x == 0) && (n >= (x * (x-1))))
			cout<<"Case #"<<i<<": GABRIEL"<<endl;
		else
			cout<<"Case #"<<i<<": RICHARD"<<endl;
	}
	
	return 0;
}
