#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;

const int N=110;
int a,n,mote[N];

int cmp(const void*x,const void *y)
{
	return *(int*)x-*(int*)y;
}

int cal(int a,int n)
{
	if(a==1) return n;
	int i,j,ret=0,ans=0;
	for(i=0;i<n;i++)
	{
		if(a<=mote[i])
		{
			if(ret==0) ans = n-i;
			else
			{
				if(ret+n-i < ans)
					ans = ret+n-i;
			}
			double tmp = mote[i]+1;
			double ta = ceil(log((tmp-a)/(a-1.0)+1.0) / log(2.0));
			ret += ta;
			a += (a-1)*(pow(2.0,ta)-1);
		}
		a+=mote[i];
		//printf("%d %d %d %d\n",i,a,ret,ans);
	}
	if(ret < ans) ans = ret;
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d%d",&a,&n);
		int i,j;
		for(i=0;i<n;i++)
			scanf("%d",&mote[i]);
		qsort(mote,n,sizeof(int),cmp);
		//for(i=0;i<n;i++)
		//	printf("%d\n",mote[i]);
		printf("Case #%d: %d\n",cnt,cal(a,n));
	} 
} 
