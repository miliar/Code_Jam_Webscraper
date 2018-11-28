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
	int t,i,n,curr,ans,x=0;
	string a;
	cin>>t;
	while(t--)
	{
		x++;
		cin>>n;
		cin>>a;
		ans=0;
		curr=a[0]-'0';
		for(i=1;i<=n;i++)
		{
			if(curr<i)
			{
				ans=ans+ i-curr;
				curr=i;
			}
			curr= curr+a[i]-'0';
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}
