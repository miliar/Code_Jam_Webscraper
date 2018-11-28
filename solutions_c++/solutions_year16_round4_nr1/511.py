#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<iostream>
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<int,int>
typedef long long LL;
using namespace std;
string ans;
bool flag;
int n,P,R,S,T;
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
bool check()
{
	string tmp=ans;
	while (tmp.size()!=1)
	{
		string t="";
		for(int i=0;i<(int)tmp.size()/2;i++)
		{
			char s1=tmp[i*2],s2=tmp[i*2+1];
			if (s1==s2) return 0;
			//R P S
			if ((s1=='R'||s2=='R')&&(s1=='P'||s2=='P')) t+='P';
			if ((s1=='R'||s2=='R')&&(s1=='S'||s2=='S')) t+='R';
			if ((s1=='P'||s2=='P')&&(s1=='S'||s2=='S')) t+='S';
		}
		tmp=t;
	}
	return 1;
}
void dfs(int step,int R,int P,int S)
{
	if (step==(1<<n)+1)
	{
		if (check())
		{
			flag=1;
		}
		return;
	}
	string tmp=ans;
	if (P)
	{
		ans=tmp+'P';
		dfs(step+1,R,P-1,S);
		if (flag) return;
		ans=tmp;
	}
	if (R)
	{
		ans=tmp+'R';
		dfs(step+1,R-1,P,S);
		if (flag) return;
		ans=tmp;
	}
	if (S)
	{
		ans=tmp+'S';
		dfs(step+1,R,P,S-1);
		if (flag) return;
		ans=tmp;
	}
}
void print(int P,int R,int S)
{
	if (P+R+S==1)
	{
		if (P) printf("P");
		if (S) printf("S");
		if (R) printf("R");
	}
	else
	{
		int sum=(P+R+S)/2;
		for(int i=P/2+1;i>=P/2;i--)
			for(int j=R/2+1;j>=R/2;j--)
				if (i+j<=sum)
			{
				int k=sum-i-j;
				if (abs(i-j)<=1&&abs(i-k)<=1&&abs(j-k)<=1)
					if (abs(P-i-R+j)<=1&&abs(P-i-S+k)<=1&&abs(R-j-S+k)<=1)
				{
					print(i,j,k);
					print(P-i,R-j,S-k);
					return;
				}
			}
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		read(n);read(R);read(P);read(S);
		if (abs(R-P)<=1&&abs(R-S)<=1&&abs(P-S)<=1)
		{
			print(P,R,S);printf("\n");
		}
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
