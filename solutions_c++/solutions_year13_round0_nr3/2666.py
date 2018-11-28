#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<queue>
using namespace std;
typedef long long LL;
const double pi=acos(-1.0);
string a[4];
bool is(int x)
{
	char s[10];
	memset(s,0,sizeof s);
	int len=sprintf(s,"%d",x);
	for(int i=0,j=len-1;i<j;i++,j--)
	{
		if(s[i]!=s[j]) return false;
	}
	return true;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int a,b;
		cin>>a>>b;
		int ans=0;
		for(int i=sqrt((double)a);i<=sqrt((double)b);i++)
		{
			if(i*i>=a && is(i) && is(i*i)) ans++;
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
	fclose(stdout);
	return 0;
}
