#include<stdio.h>
int main()
{
    freopen("input.in", "r", stdin);
   freopen("output.out", "w", stdout);
    int t,y=0;
    scanf("%d",&t);
    while(y<t)
    {
	int n,i,j,k,a,b,c,p,flag;
	int arr[10];
	i=0;
	
	scanf("%d",&n);
	if(n==0)
	{
	    printf("Case #%d: INSOMNIA\n",y+1);
	}
	else
	{
	if(n<10)
	{
		arr[i]=n; i++ ;
	}
	else if(n>=10 && n<100)
	{
		a=n%10;
		b=(n/10)%10;
		if(a==b)
		{
			arr[i]=a; i++;
		}
		else
		{
			arr[i]=a; arr[i+1]=b; i+=2;
		}
	}
	
	else if(n>=100 && n<=200)
	{
		a=n%10;  b=(n/10)%10;  c=((n/10)/10)%10;
		if(a!=b && a!=c && b!=c)
		{
			arr[i]=a;  arr[i+1]=b;  arr[i+2]=c;  i+=3;
		}
		else if(a==b && b==c)
		{
			arr[i]=a;  i++;
		}
	    else if(a!=b && b==c)
		{
			arr[i]=a;  arr[i+1]=b;  i+=2;
		}
		
		else if(a==b && b!=c)
		{
			arr[i]=a;  arr[i+1]=c;  i+=2;
		}
		else if(a==c && a!=b)
		{
			arr[i]=a; arr[i+1]=b; i+=2;
		}
	}
	for(j=2;i<10;j++)
	{
		a=n*j;  p=a;
		while(a!=0)
		{	flag=1;
			b=a%10; a/=10; 
			for(k=0;k<i;k++)
			{
				if(b==arr[k])
				{
					flag=0;  break;
				}
			}
			if(flag!=0)
			{
				arr[i]=b; 
				 i++;
		 }
			
		}
	}
	if(i==10)
	printf("Case #%d: %d\n",y+1,p);
	else
	printf("Case #%d: INSOMNIA",y+1);
    }
    y++;
    }
	return 0;
}
