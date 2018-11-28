/* ***********************************************
Author        :dingyuyang 
Created Time  :六  4/ 9 09:39:31 2016
File Name     :c.cpp
************************************************ */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
#define ll long long
const int inf=0x3f3f3f3f;
const ll llinf=0x3f3f3f3f3f3f3f3f;
const double finf=9999999999.0;
char s[1000],sz;
int d[12];
void print()
{
	printf("%s",s);
	for(int i=2;i<=10;i++) printf(" %d",d[i]);
	printf("\n");
}
void getstr(ll num)
{
	int ptr=0;
	for(;num;num>>=1)
	{
		s[ptr++]=(num&1)+'0';
	}
	reverse(s,s+ptr);
	s[ptr]=0;
	sz=strlen(s);
}
int getd(int bs)
{
	ll num=0;
	for(int i=0;i<sz;i++)
	{
		int dg=s[i]-'0';
		num=num*bs;
		num+=dg;
	}
	int flg=0,i;
	int lim=sqrt(num);
	//printf("num=%lld\n",num);
	if(num==2) flg=1;
	else{
	for(i=2;i<=lim+1&&i<=num;i++)
	{
		//printf("i=%d\n",i);
		if(num%i==0)
		{
			flg=1;
			break;
		}
	}
	}
	if(!flg) return 0;
	else
	{
		d[bs]=i;
		return 1;
	}
}
bool check()
{	
	if(s[0]!='1'||s[sz-1]!='1') return 0;
	for(int i=2;i<=10;i++)
	{
	//	printf("i=%d\n",i);
		if(getd(i)==0) return 0;
	}
	return 1;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
	scanf("%d",&T);
	printf("Case #1:\n");
	int N,J;
	scanf("%d%d",&N,&J);
	int cnt=0;
	ll l=(1LL<<(N-1)),h=1LL<<N;

	for(ll i=h;i>=l;i--)
	{
		//printf("i=%lld\n",i);
		getstr(i);
		//printf("%s\n",s);
		if(check())
		{
			cnt++;
			print();
		}
		if(cnt==J) break;
	}
    return 0;
}
