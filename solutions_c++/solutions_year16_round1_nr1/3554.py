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
		string s, ans;
		cin>>s;
		ans = ans + s[0];
		for(int j = 1; s[j] != '\0'; j++)
		{
		    if((int)ans[0] > s[j])
		        ans = ans + s[j];
		    else
		        ans = s[j] + ans;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
	return 0;
}
