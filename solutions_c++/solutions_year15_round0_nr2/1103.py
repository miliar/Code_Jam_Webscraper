#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
using namespace std;
#define llu long long unsigned int
#define lli long long int
#define li long int
#define fi first
#define se second
#define pb push_back
#define vi vector<int>
#define mod 1000000007
int scan()    {int ip=getchar_unlocked(),ret=0,flag=1;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
li scanli()    {int ip=getchar_unlocked(),flag=1;li ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
lli scanlli()    {int ip=getchar_unlocked(),flag=1;lli ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
llu scanllu()    {int ip=getchar_unlocked();llu ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked());for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return ret;}
void print(int n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=10;char output_buffer[10];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<10);}
void printli(li n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=11;char output_buffer[11];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<11);}
void printlli(lli n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<21);}
void printllu(llu n)     {int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<21);}

lli a[1001];

int main()
{	
	lli t=scan(),i,j,k;
	for(k=1;k<=t;k++)
	{
		lli d=scan();
		for(i=0;i<d;i++)
			a[i]=scan();
		lli ans,ans1;
		for(i=1;i<=1000;i++)
		{
			ans=i;
			for(j=0;j<d;j++)
			{
				if(a[j]>i)
				{
					if(a[j]%i==0)
						ans+=(a[j]/i-1);
					else
						ans+=(a[j]/i);
				}
			}
			if(i==1)
				ans1=ans;
			else
				ans1=min(ans1,ans);
		}
		cout<<"Case #"<<k<<": "<<ans1<<endl;
	}
	return 0;
}
