#include<bits/stdc++.h>
using namespace std;
#define mem(arr,x) memset(arr,x,sizeof(arr))

typedef long long LL;



main() {
	FILE *fin = freopen("B-small.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("B-small.out", "w", stdout);
	int t,n,ans,count=0;
	char s[200];
	int dp[105];

	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin>>s;
		mem(dp,0);
		//dp[0][0]=1;
		//dp[0][1]=0;
		ans=0;
		//i=0;
		count=0;
		n=strlen(s);
		int j=1;
		
		//while(s[j]==s[j-1])j++;
		//if(s[j-1]=='-')ans=1;
		
		while(j<=n){
			while(s[j]==s[j-1])j++;
			if(s[j-1]=='+' && count==0)count=1;
			if(s[j-1]=='-' && count!=0){
				ans+=2;
				//count--;
			}
			else if(s[j-1]=='-' && count==0){
				ans=1;
				count=1;
			}
			j++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;

	}
	exit(0);
}