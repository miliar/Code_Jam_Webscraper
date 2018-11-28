#include <stdio.h>
#include <algorithm>
using namespace  std;

__int64 ppp[10000],cntppp;

__int64 makep(int x,int ignoer)
{
	__int64 ret = x;
	int dig;
	while (x)
	{
		if ( !ignoer )
		{
			dig = x%10;
			ret = ret *10 + dig;
		}
		x /= 10;
		if (ignoer) ignoer --;
	}
	return ret;
}

char buf[64];
int isppp( __int64 x )
{
	int len = 0,i,j;
	while (x)
	{
		buf[len++] = x%10;
		x/=10;
	}
	for ( i=0,j=len-1 ;i<j; ++i,--j )
	{
		if ( buf[i] != buf[j] ) return 0;
	}
	return 1;
}


int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	__int64 root,pp;
	int i;
	cntppp = 0;
	for ( i=1;i<=100000;++i )
	{
		root = makep(i,0);
		pp = root * root;
		if ( isppp(pp) )
		{
			ppp[cntppp++] = pp;
			//printf("base %-7d root %-10I64d -> power %-16I64d\n",i,root,pp);	
		}
		root = makep(i,1);
		pp = root * root;
		if ( isppp(pp) )
		{
			ppp[cntppp++] = pp;
			//printf("base %-7d root %-10I64d -> power %-16I64d\n",i,root,pp);	
		}
	}
	sort(ppp, ppp + cntppp);


	int t,st,low,up;
	__int64 s,e;
	scanf("%d",&st);
	for ( t=1;t<=st;++t )
	{
		scanf("%I64d%I64d",&s,&e);
		for ( low = 0; low<cntppp; ++low )
			if ( ppp[low] >= s ) break;
		for ( up=cntppp-1;up>=0;--up )
			if ( ppp[up] <= e ) break;
		printf("Case #%d: %d\n",t,up-low+1);
	}

	return 0;
}

