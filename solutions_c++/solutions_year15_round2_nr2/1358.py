#include<stdio.h>
#include<algorithm>

using namespace std;
#define INF 100000

int row,col,n;

int power(int a,int n);
int adj(int r1,int c1, int r2, int c2);
int on(int i, int pos);

int on(int i, int pos)
{
	return i & (1<<pos);
}

int adj(int r1,int c1, int r2, int c2)
{
	if(r1==r2 && (c1-c2 == 1 || c2-c1==1))
		return 1;
	if(c1==c2 && (r2-r1==1 || r1-r2==1))
		return 1;
	return 0;
}

int power(int a,int n)
{
	if(a==0)
		return 0;
	if(n==0)
		return 1;
	int ret = power(a, n/2);
	if(n&1)
		return ret*ret*a;
	else
		return ret*ret;
}

int popcount(int a)
{
	int i=0,b=a;
	while(b> 0)
	{
		if(b&1)
			++i;
		b/=2;

	}
	return i;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ti,i,res,p,q,cur,r,c;
	scanf("%d",&t);
	for(ti=1; ti<=t; ++ti)
	{
		res = INF;
		scanf("%d %d %d",&row, &col, &n);
		for(i=0; i<power(2, row*col); ++i)
		{
			if(popcount(i) == n)
			{
				cur=0;
				for(p=0; p<row*col; ++p)
				{
				
					if(on(i,p))
					{
						for(q=p+1; q<row*col; ++q)
						{
							if(!on(i,q))
								continue;
							r=q/col;
							c=q%col;
							if(adj(p/col,p%col,r,c))
								cur++;
						}
					}
				}
				res=min(res,cur);
			}
		}
		printf("Case #%d: %d\n",ti,res);
	}
	return 0;
}