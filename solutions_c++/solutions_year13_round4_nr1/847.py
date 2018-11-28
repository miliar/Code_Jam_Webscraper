#include <stdio.h>
struct inout{
	int p;
	bool in;
	int num;
} x[2500],y[2500],k;
void sort(int n)
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			if(x[i].p>x[j].p||(x[i].p==x[j].p&&!x[i].in&&x[j].in))
			{
				k=x[j];
				x[j]=x[i];
				x[i]=k;
			}
}
int main()
{
	int t,i,j,n,m,a,b,c,top;
	long long now;
	FILE *in= fopen("a.in","r");
	FILE *out= fopen("a.out","w");
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(in,"%d%d",&n,&m);
		now=0;
		for(j=0;j<m;j++)
		{
			fscanf(in,"%d%d%d",&a,&b,&c);
			k.p=a,k.in=1,k.num=c;
			x[j*2]=k;
			k.p=b,k.in=0,k.num=c;
			x[j*2+1]=k;
			now+=((long long)(b-a)*(long long)(b-a-1)/(long long)2)*((long long)c);
		}
		sort(2*m);top=-1;
		for(j=0;j<2*m;j++)
		{
			if(x[j].in)
				y[++top]=x[j];
			else 
			{
				c=x[j].num;b=x[j].p;
				while(c!=0)
				{

					if(c>=y[top].num)
					{
						a=y[top].p;
						now-=((long long)(b-a)*(long long)(b-a-1)/(long long)2)*((long long)y[top].num);
						c-=y[top].num;
						top--;
					}
					else
					{
						a=y[top].p;
						now-=((long long)(b-a)*(long long)(b-a-1)/(long long)2)*((long long)c);
						y[top].num-=c;
						c=0;
					}
				}
			}
		}
		fprintf(out,"Case #%d: %lld\n",i,-now);
	}
	return 0;
}
