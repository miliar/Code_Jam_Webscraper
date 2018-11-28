#include<stdio.h>
#include<string.h>
#include<math.h>
long long int isPrime(long long int n)
{
	int flag=0;
	long long int i;
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		{
			flag = 1;
			break;
		}
	}
	if(flag==0)
		return 0;
	else
		return i;
}

int main()
{
	int t,n,j,k=0;
	scanf("%d",&t);
	while(k!=t)
	{
		scanf("%d",&n);
		scanf("%d",&j);
		printf("Case#%d:\n",k+1);		
		int temp,a[50];
		long long int i,d,n1;
		long long int b[10];
		int m,x,y,c=0,l=0;
		long long int ul = pow(2,n);
		long long int ll = pow(2,(n-1))+1;
		for(i=ll;i<ul;i=i+2)
		{
			l=0;
			c=0;
			d = isPrime(i);
			//printf("%lld",d);
			if(d!=0)
			{
           			b[c++] = d;
				n1 = i;
				while(n1!=0)
				{
  					a[l++] = n1%2;
					n1 = n1/2;
				}				
				for(x=3;x<=10;x++)
				{
					n1 = 0;
					for(y=0;y<l;y++)
					{
						n1 = n1 + (a[y]*pow(x,y));
					}	
					//printf("%lld \n",n1);
					d = isPrime(n1);
					if(d!=0)
					b[c++] = d;
					else
					break;
				}
				if(x==11)
				{
					for(x=0;x<l/2;x++)
					{
					temp = a[x];
					a[x] = a[l-x-1];
					a[l-x-1] = temp;
					}
					for(y=0;y<l;y++)
					{
						printf("%d",a[y]);
					}
					for(y=0;y<9;y++)
					{
						printf(" %lld",b[y]);
					}
					printf("\n");
					j--;
					if(j==0)
						break;
				}
		     }			
	               
		}
		k++;
	}
	return 0;
}
