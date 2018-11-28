/*
name:Hatsune_Miku
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char s[105];
int a[105];
int solve(int n,int f)
{
	if(n==1) return f!=a[0];
	int p1=0,p2=0;
	for(int i=n;i>=1;i--)
	{
		if(a[i-1]==f) continue;
		p1=i;
		break; 
	}
	if(p1==0) return 0;
	for(int i=p1;i>=1;i--)
	{
		if(a[i-1]!=f) continue;
		p2=i;
		break;
	}
	if(p2==0) return 1;
	return solve(p2,1-f)+1;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int temp=T;
	while(T--){
		cin>>s;
		for(int i=0;i<strlen(s);i++)
		{
			if(s[i]=='+') a[i]=1;
			else a[i]=0;
		}
		int ans=solve(strlen(s),1);
		printf("Case #%d: %d\n",temp-T,ans);
	}
	return 0;
}
