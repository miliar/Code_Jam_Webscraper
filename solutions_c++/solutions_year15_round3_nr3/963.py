#include "stdio.h"
#include "string.h"

#if 1

//#define F	"C-large"
#define F	"C-small-attempt2"
#ifndef F
#define TEST	1
#define F	"C"
#endif
//#define TEST	1

//typedef long long _int;
typedef int _int;

#define P	printf

#define N	7

int n, a[N], b[43], vst[N], val, v;

void dfs(int i)
{
	vst[i] = 1;

	val += a[i];
	if(val <= v)
	{
		b[val]++;

		for(int j=0 ; j<n ; ++j)
		{
			if(!vst[j])
				dfs(j);
		}
	}
	val -= a[i];
	vst[i] = 0;
}

int main(void)
{
	freopen("IO/"F".in","r",stdin);
#ifndef TEST
	freopen("IO/"F".out.txt","w",stdout);
#endif
	int t,tst=1;
	scanf("%d", &tst);
	for(t=1 ; t<=tst ; ++t)
	{
		P("Case #%d: ",t);
		_int i,j,k;
		scanf("%d %d %d", &i, &n, &v);
		for(i=0 ; i<n ; ++i)
			scanf("%d", a+i);
		memset(b,0,sizeof(b[0])*(v+3));
#ifdef TEST
		P("[%d %d] ", n, v);
		for(i=0 ; i<n ; ++i)
		{
			P("%d ", a[i]);
		}
#endif

		for(i=0 ; i<n ; ++i)
		{
			val = 0;
			memset(vst,0,sizeof(vst));
			dfs(i);
		}

#ifdef TEST
		P("[");
		for(i=1 ; i<=v ; ++i)
		{
			if(b[i])
				P("%d,", i);
		}
		P("] ");
#endif
		for(i=1,j=0 ; i<=v ; ++i)
		{
			if(!b[i])
			{
#ifdef TEST
				P("(%d)",i);
#endif
				j++;
				//for(k=i+1 ; k<=v && k<=(i+i-1) ; ++k)
				//	b[k]++;
				for(k=(v-i) ; k ; --k)
					if(b[k])
						b[k+i]++;
				b[i]++;
			}
		}

#ifdef TEST
		P("\t");
#endif
		P("%d\n",j);
	}
	return 0;
}

#endif


