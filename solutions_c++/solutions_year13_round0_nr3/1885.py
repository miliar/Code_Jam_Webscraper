#include<stdio.h>
#include<math.h>
int main()
{
	long long int c,i,j,k,l,r,m;
	int t;
	long long int a,b,y,z;
	long long int  p;
	//char a[5][5],junk;
	freopen("in2l.in","r",stdin);
	freopen("test_out.txt","w",stdout);
	
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{//printf("5");
	//	scanf("%s %s",a,b);
	//	printf("%s %s",a,b);
	//	printf("6");
		/*for(j=a;j<=b;j++)
		{
			k=j;
			while
		}*/
		c=0;
		scanf("%lld %lld",&a,&b);
		//printf("%lld %lld",a,b);
	//	printf("%d %d\n",a,b);
		y=sqrt(a);
		z=sqrt(b);	
		for(j=y;j<=z;j++)
		{
			k=j;
			l=0;
			while(k!=0)
			{
				r=k%10;
				l=l*10+r;
				k=k/10;
			}
			//printf("%lld  ",l);
			//printf("%d\n",l);
			if(l==j)
			{
			//	printf("%d ",l);
				p=pow(j,2);
				m=p;
				//if(p==m)
				//{
						k=m;
						l=0;
						while(k!=0)
						{
							r=k%10;
							l=l*10+r;
							k=k/10;
						}
						if(l==p&&p>=a&&p<=b)
						{
								c++;		
				//		printf("%d " ,l);
						}		
				//}	
			}
		}
			printf("Case #%d: %d\n",i,c);
		
	}							
		//printf("%d\n",w);
	
	return 0;
}
