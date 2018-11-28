#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<stdlib.h>


using namespace std;

int hcf(int a,int b)
{
	int hcf,i;
	for(i=1; i<=a || i<=b; ++i)
    {
        if(a%i==0 && b%i==0)   /* Checking whether i is a factor of both number */
            hcf=i;
    }
    
    return hcf;
}

int main()
{
	int t,c,f;
	double z=1;
	char str[100],num[50],den[50];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%s",str);
		int k;
		for(k=0;k<strlen(str);k++)
		{
			if(str[k] == '/')
				break;
				
			num[k] = str[k];	
		}
		num[k] = '\0';
		int l=0;
		k++;
		for(l=0;k<strlen(str);l++,k++)
		{
			den[l] = str[k];
			
		}
		
		den[l] = '\0';
		
		
		int p = atoi(num);
		int q = atoi(den);
		c=0;
		
		
		//cout<<" "<<p<<" "<<q;

		int o=hcf(p,q);
		p=p/o;
		q=q/o;
		
		//cout<<p<<" "<<q;

		double e=(double)p/q;
			
		z=1;
		
		for(int y=1;y<=40;y++)
		{
			f=0;
			z=z*2;
			if(q == z)
			{	f=1;
				break;	
			}
		}
		
		z=1;
		
		if(f==0)
			printf("Case #%d: impossible\n",i);
		else
		{
			for(int y=1;y<=40;y=y++)
			{	
				c++;
				z=z/2;
				if(e >= z)
				{	break;	
				}
			}
			printf("Case #%d: %d\n",i,c);
		
		}
		
	}
		
}
	
