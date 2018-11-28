#include<iostream>
#include<map>
#include<algorithm>
#include<math.h>
#include<stack>
#include<queue>
#include<string.h>
#include<vector>
#include<iomanip>
#include<cstdio>
#include<set>
#define REP(i,n)	for(int i=0;i<n;i++)
#define RE(i,j,n)	for(int i=j;i<n;i++)
using namespace std;
typedef long long LL;
typedef long L;
int main()
{
	//ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int n;
	REP(z,t)
	{
		int s;
		cin>>s;
		string str;
		cin>>str;
		int ans=0;
		int i=0;
		int sum=str[i]-'0';
		for(i=1;i<=s;i++)
		{
			 int val=str[i]-'0';
			 if(i>sum)
			 {
			 	ans+=i-sum;
			 	sum+=i-sum;
			 }
			 sum+=val;

		}
		cout<<"Case #"<<z+1<<": "<<ans<<endl;
	}
	return 0;
}
