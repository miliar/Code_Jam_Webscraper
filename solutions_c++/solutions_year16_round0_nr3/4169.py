#include<iostream>
#include<cmath>
#define lim 1111111111111111
//#define lim 111111
FILE *out;

bool possible[11];
int divisors[11];

long long powC(long long a, long long b)
{	
	//printf("....calculating pow\n");
	if(b==0)
	return 1;
	else
	{
		long long temp=pow(a,b/2);
		if(b%2==0ll)
		return temp*1ll*temp;
		else
		return temp*1ll*temp*a;
	}
}

long long isPrime(long long x)
{
	int root=(int)floor(sqrt(x));
	//printf("....calculating prime x=%d\n",x);
	long long i;
	for(i=2;i<=root;++i)
	{
		if(i%1000000==0)	
		printf("....i=%d\n",i);
		if(x%i==0)
		return i;
	}
	return -1;
}

int main(){
	long long i,j,k,temp,num,count=0;
	bool valid;
	out = fopen("out.txt","w");	
	fprintf(out,"Case #1:\n");
	for(i=powC(2,15);i<=lim;++i)
	{	
		if(i%1000000==0)			
		printf("..%lld\n",i);	
		if(((1&i)>0) && ((powC(2,15)&i)>0))
		{
			for(j=2;j<=10;++j)
			{				
				possible[j]=false;
				divisors[j]=-1;
			}
			//printf("..possiblity\n",i);
			for(j=2;j<=10;++j)
			{
				num=0;
				for(k=0;k<16;++k)
				{
					if((powC(2,k)&i)>0)
					num+=powC(j,k);
				}
				temp=isPrime(num);
				if(temp!=-1)
				{				
					possible[j]=true;
					divisors[j]=temp;
				}
				else
				{
					break;
				}
			}			
			valid=true;
			for(j=2;j<=10;++j)
			{
				if(possible[j]==false)
				{
					valid=false;
					break;
				}			
			}
			if(valid)
			{
				for(j=15;j>=0;--j)
				{
					if((powC(2,j)&i)>0)
					{	
						fprintf(out,"1");
						printf("1");
					}
					else
					{
						fprintf(out,"0");
						printf("0");					
					}
				}
				fprintf(out," ");
				printf(" ");
				for(j=2;j<=10;++j)
				{							
					fprintf(out,"%d ",divisors[j]);
					printf("%d ",divisors[j]);
				}
				fprintf(out,"\n");
				printf("\n");
				++count;
				printf("..count=%d\n",count);						
			}
		}
		if(count>=50)
		break;
		
	}
	printf("....end!\n");
	return 0;
}
