#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <stack>
#include <queue>
#include <set>
#include <map>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a>b?b:a
#define GCD(a,b)  { return (b==0)?a:GCD(b,a%b);
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR_X(i,n,x) for(i=x;i<n;i++)
#define BACK(i,n) for(i=n;i>=0;i--)
#define BACK_X(i,n,x) for(i=n;i>=x;i--)

typedef long long int lld;
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0); //dont use with EOF
	int t,i,j,x=0,n;
	int a[1002];
	cin>>t;
	while(t--)
	{
		x++;
		cin>>n;
		int max=0;
		FOR(i,n)
		{
			cin>>a[i];
			max=MAX(max,a[i]);
		}
		int ans=max;
		for(i=1;i<=max;i++)
		{
			int thi=0;
			FOR(j,n)
			{
				thi= thi + (a[j]+i-1)/i-1;
			}
			ans=MIN(ans,thi+i);
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}

