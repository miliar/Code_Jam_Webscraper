#include<stdio.h>
#include<math.h>
int main()
{
long long int i,pwr[18][18],k=50,j,temp,index,t,sp,a[20],sum,p,fact[18],flag,lp,count=0,n=16;

FILE *fp=fopen("a.in","r");
FILE *fp2 = fopen("cb.out","w");

for(i=1;i<=17;i++)
{
	pwr[i][0]=1;
}

for(i=1;i<=17;i++)
{
	k=1;
	for(j=1;j<17;j++)
	{
		k=k*i;
		pwr[i][j]=k;
	//	k=k*i;
	}
}

fprintf(fp2,"Case #1:\n");
for(i=32769;; i+=2)
{
	temp=i; index=1;
	while(temp>0)
	{
		t=temp%2;
		a[index]=t;
		index++;
		temp=temp/2;
	}

	for(sp=2;sp<11;sp++)
	{
    	sum=0;
		for(j=1;j<=16;j++)
		{
			sum=sum+(pwr[sp][j-1]*a[j]);
		}
	
		//if(i==10&&sum%2==0)
    	//sum++;
    

for(p=3;p<=sqrt(sum);p=p+2)
{
if(sum%p==0)
{
	fact[sp]=p;
	flag=0;
	break;
}
}

if(p>sqrt(sum))
{
    goto XXX;
}

if(sp==10)
{
   	 	for(lp=16;lp>=1;lp--)
    	fprintf(fp2,"%lld",a[lp]);
    //	printf(" ");
    	for(lp=2;lp<=10;lp++)
    	fprintf(fp2," %lld",fact[lp]);
    	fprintf(fp2,"\n");
    
     count++;
     if(count>=50)
     goto Y;
 }
}
XXX:{}
}

Y: {}
return 0;
}
