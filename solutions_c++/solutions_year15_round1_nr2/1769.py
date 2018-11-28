#include <stdio.h>
#include <queue>

using namespace std;

long long GCD(long long a,long long b)
{
	//printf("%I64d %I64d\n",a,b);
	if(b==0) return a;
	return GCD(b,a%b);
}

struct pt
{
	int t,in;
	bool operator<(const pt &a)const
	{
		if(t > a.t)
			return true;
		if(t < a.t)
			return false;
		if(in > a.in)
			return true;
		return false;
	}
};

priority_queue<pt >q;
pt tmp;
int x[1200];
long long gcd,mul=1;

int main()
{
	int Q,i,j,n,k,count;
	int m;
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	scanf("%d",&Q);
	for(k=1;k<=Q;k++)
	{
	    mul=1,gcd=1,count=0;
		scanf("%d %d",&n,&m);
		scanf("%d",&x[1]);
		mul=gcd=x[1];
		tmp.t=0;
		tmp.in=1;
		q.push(tmp);
		for(i=2;i<=n;i++)
		{
			scanf("%d",&x[i]);
			mul=mul*x[i];
			// printf(" + %d\n",mul);
			gcd=GCD((long long)x[i],gcd);
			// printf("- %d\n",gcd);
			mul/=gcd;
			// printf(" %d\n",mul);
			tmp.t=0;
			tmp.in=i;
			q.push(tmp);
		}
		// printf("%d\n",mul);
		for(i=1;i<=n;i++)
            count+=mul/x[i];
        // printf("%d\n",count);
		m%=count;
		if(m==0)
			m=count;
		// printf("%d\n",m);
		for(i=1;i<m;i++)
		{
			tmp=q.top();
			q.pop();
			tmp.t+=x[tmp.in];
			q.push(tmp);
		}
		printf("Case #%d: %d\n",k,q.top().in);
		while(!q.empty())
			q.pop();
	}
	return 0;
}
