#include <cmath> 
#include <cctype>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define DBG cout<<"HERE"<<endl;

bool cmp(const int a, const int b)
{
	return a > b;
}

int sig(int a,int b)
{
	return a/abs(a) * b/abs(b);	
}

int mul(int a,int b) //1-1 2-i 3-j 4-k
{
	if(a<0 || b<0) return sig(a,b) * mul(abs(a),abs(b));
	if(a==1) return b;
	if(b==1) return a;
	if(a==b) return -1;
	if(a>b) return -mul(b,a);
	if(a==2 && b==3) return 4;
	if(a==2 && b==4) return -3;
	if(a==3 && b==4) return 2;
	return 0;
}

int mulc(int a,char b)
{
	int bb= b-'g';
	return mul(a,bb);
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int cases=0;	cin>>cases;
	int dp[10086]={0};
	for(int _case=1;_case<=cases;_case++)
	{
		int l,x;	string ss,s="";
		cin>>l>>x>>ss;
		l=l*x;
		for(int i=0;i<x;i++) s+=ss; //cout<<s<<endl;
		if(l<3)
		{
			printf("Case #%d: NO\n",_case);
			continue;
		}
		dp[0]=mulc(1,s[0]);
		int flag=0;
		for(int i=0;i<l;i++)
		{
			if(i) dp[i]=mulc(dp[i-1],s[i]);
			//cout<<i<<":"<<dp[i]<<endl;
			if(flag==0)
			{
				if(dp[i]==2) flag=1;	
			}
			else if(flag==1)
			{
				//cout<<"1!"<<endl;
				if(dp[i]==4) flag=2;
			} 
			else if(flag==2)
			{
				//cout<<"2!"<<endl;
			} 
		}
		//cout<<dp[l-1]<<endl;
		bool f = (flag==2) && (dp[l-1]==-1);
		printf("Case #%d: ",_case);
		if(f)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

