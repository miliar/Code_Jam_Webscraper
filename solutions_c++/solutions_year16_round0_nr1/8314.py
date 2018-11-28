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
long long int n,tmp,tmp2;
int cnt,t,i,x,num;
bool mark[12];
int main()
{
	freopen("A-large.in", "r",stdin);
    freopen("out1.txt", "w" ,stdout);
	s(t);
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
			num++;
			printf("Case #%d: INSOMNIA\n",num);
		}
		else
		{
			for(i=0;i<=9;i++)
			mark[i]=0;
			cnt=10;
			tmp=n;
			while(cnt>0)
			{
				tmp2=tmp;
				while(tmp)
				{
					x=tmp%10;
					tmp=tmp/10;
					if(mark[x]==0)
					{
						mark[x]=1;
						cnt--;
					}	
				}
				tmp=tmp2+n;
			}
			tmp=tmp-n;
			//cout<<tmp<<" ";
			//tmp=tmp/n;
			num++;
			printf("Case #%d: %lld\n",num,tmp);
		}
	}
	return 0;
	
}
