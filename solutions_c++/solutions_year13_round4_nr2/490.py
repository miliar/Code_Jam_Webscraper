//nathanajah's template
//28-11-2012
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <ctime>
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned LL
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#ifdef DEBUG
	#define debug(...) \
	fprintf(stderr,__VA_ARGS__)
#else
	#define debug(...) 
#endif
using namespace std;

inline string GetString()
{
	char GS[1000005];
	scanf("%s",GS);string ret=GS;
	return ret;
}

inline char getc()
{
	char c=' ';
	while (c==' ' || c=='\t' || c=='\r' || c=='\n')
		c=getchar();
	return c;
}
//ENDOFTEMPLATE

LL t,n,aaaa;
LL p;
LL i;
LL hitungb(LL x)
{
	string s="";
	LL i;
	LL menangdari=x;
	for (i=n-1;i>=0;--i)
	{
		if (menangdari+1==(1LL<<(i+1)))
		{
			s.append(1,'L');
			break;
		}
		else
			s.append(1,'W');
		menangdari=(menangdari+1)/2;
	}
	while (SZ(s)<n)
		s.append(1,'L');
	LL ret=0;
	for (i=0;i<SZ(s);++i)
	{
		if (s[i]=='L')
			ret=2*ret+1;
		else
			ret=2*ret;
	}
	return ret;
}

LL hitungw(LL x)
{
	string s="";
	LL i;
	LL menangdari=x;
	for (i=n-1;i>=0;--i)
	{
		if (menangdari==0)
		{
			s.append(1,'W');
		}
		else
		{
			s.append(1,'L');
			--menangdari;
			menangdari=(menangdari)/2;
		}
	}
	LL ret=0;
	for (i=0;i<SZ(s);++i)
	{
		if (s[i]=='L')
			ret=2*ret+1;
		else
			ret=2*ret;
	}
	return ret;
}

int main()
{
	scanf("%I64d",&t);
	for (aaaa=0;aaaa<t;++aaaa)
	{
		printf("Case #%I64d:",aaaa+1);
		scanf("%I64d %I64d",&n,&p);
		LL l=0;
		LL r=(1LL<<n)-1;
		LL mid=(l+r)/2;
		while (l<r)
		{
			if (hitungw(mid)<p)
			{
				l=mid;
				mid=(l+r+1)/2;
			}
			else
			{
				r=mid-1;
				mid=(l+r)/2;
			}
		}
		printf(" %I64d",mid);
		
		l=0;
		r = (1LL<<n)-1;
		mid=(l+r)/2;
		while (l<r)
		{
			if (hitungb(mid)<p)
			{
				l=mid;
				mid=(l+r+1)/2;
			}
			else
			{
				r=mid-1;
				mid=(l+r)/2;
			}
		}
		printf(" %I64d\n",mid);
	}
}
