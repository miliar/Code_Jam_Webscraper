#if 1
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <map>

#define TEST	0

#define P	printf

#if TEST
#define P2	printf
#endif

#define F	"C-small-attempt3"
#ifndef F
#define F	"R0-3"
#endif
#ifndef P2
#define P2
#endif

#define N	10000

using namespace std;

char s[N+10];

char a[5][5][2] = {
		{	{0,0}, {0,0}, {0,0}, {0,0}, {0,0},	},
		{	{0,0}, {0,1}, {0,2}, {0,3}, {0,4},	},
		{	{0,0}, {0,2}, {1,1}, {0,4}, {1,3},	},
		{	{0,0}, {0,3}, {1,4}, {1,1}, {0,2},	},
		{	{0,0}, {0,4}, {0,3}, {1,2}, {1,1},	}
};

const char* ans[] = {"NO", "YES"};

int main(void)
{
	freopen("IO/"F".in","r",stdin);
	freopen("IO/"F".out.txt","w",stdout);

	int t,tst;
	scanf("%d", &tst);
	for(t=1 ; t<=tst ; ++t)
	{
		map<int,int> mk;
		int i=1,j,k,l,x,n,m,r=0,c,m2,c2,lmt=-1;
		scanf("%d %d %s", &l, &x, s);

		if(l*x < 3)
		{
			i = 1;
			goto ANS;
		}

		for(j=0 ; j<l ; ++j)
		{
			s[j] -= 'i'-2;
		}

		n = l;
		for(i=1 ; i<x ; ++i)
		{
			for(j=0 ; j<l ; ++j)
			{
				s[n++] = s[j];
			}
		}
		s[n] = 0;
//		for(i=0 ; i<n ; ++i)
//			P("%d", s[i]);

#if 0
		m2 = 0;
		c2 = s[0];
		if(c2==4)
		{
			P("%d,", 0);
		}
		for(k=1 ; k<n ; ++k)
		{
			char* p = a[c2][s[k]];
			m2 += p[0];
			c2 = p[1];
			if(!(m2&1) && c2==4)
			{
				P("%d,", k);
			}
		}
#endif

		i = 1;
		m = 0;
		c = s[0];
		if(c!=2)
		{
			for( ; i<n-2 && ((m&1) || c!=2); ++i)
			{
				char* p = a[c][s[i]];
				m += p[0];
				c = p[1];
			}
			if((m&1) || c!=2)
			{
				i = 2;
				goto ANS;
			}
		}
		P2("I%d,",i);

		m2 = 0;
		c2 = s[n-1];
		if(c2==4)
		{
			lmt=n-1;
			mk[n-1] = 1;
			P2("K%d,",n-1);
		}
		for(k=n-2 ; k>i ; --k)
		{
			char* p = a[s[k]][c2];
			m2 += p[0];
			c2 = p[1];
			if(!(m2&1) && c2==4)
			{
				if(lmt<0)
					lmt=k;
				mk[k] = 1;
				P2("K%d,",k);
			}
		}
		if(lmt<0)
		{
			i = 4;
			goto ANS;
		}
		P2("lmt=%d,",lmt);

		r = 1;
AGAIN:
		m2 = 0;
		c2 = s[i];
		if( (c2==3) && (mk.find(i+1) != mk.end()) )
		{
			i = 30;
			P2("J%d,",i);
			goto ANS;
		}
		for(j=i+1 ; j<lmt ; ++j)
		{
			char* p = a[c2][s[j]];
			m2 += p[0];
			c2 = p[1];
			if(!(m2&1) && (c2==3))
			{
				P2("J%d,",j);
				if(mk.find(j+1) != mk.end())
				{
					i = 31;
					goto ANS;
				}
			}
		}
		// Find next i loc
		for( ; i<lmt ; ++i)
		{
			char* p = a[c][s[i]];
			m += p[0];
			c = p[1];
			if(!(m&1) && c==2)
			{
				i++;
				P2("I%d,",i);
				goto AGAIN;
			}
		}
		r = 0;
		i = 3;
ANS:
#if !TEST
		P("Case #%d: %s\n",t,ans[r]);
#else
		if(r==0 && i==3)
		P("Case #%d: %6d %6d %d %s\n",t,l,x,i,ans[r]);
#endif
	}
	return 0;
}
#endif

