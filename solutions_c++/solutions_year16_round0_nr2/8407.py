#include<stdio.h>
#include<iostream>
#include<string.h>
#include<map>
#include<math.h>
#include<queue>
#include<limits.h>
#include<algorithm>
#include<vector>
#define s(n) scanf(" %d",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf(" %d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define M 1000000007LL
using namespace std;
int t,i,cnt,num,n;
char str[104];
int main()
{
	freopen("B-large.in", "r",stdin);
    freopen("out2.txt", "w" ,stdout);
	s(t);
	while(t--)
	{
		scanf(" %s",str);
		n=strlen(str);
		cnt=0;
		i=0;
		if(str[i]=='-')
		{
			cnt++;
			i++;
		}
		while(i<n && str[i]!='+')
		{
			i++;
		}
		for(;i<n;)
		{
			while(i<n && str[i]!='-')
			i++;
			//cnt+=2;
			if(i<n)
			cnt+=2;
			while(i<n && str[i]!='+')
			i++;
		}
		num++;
		printf("Case #%d: %d\n",num,cnt);
	}
	return 0;
}
