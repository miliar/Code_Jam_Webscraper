#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;



int main(void)
{
	int  count,i,j,k,a,b,tmp,cas,cases;
	char ch;
	char num[40];
	char re[40];
	double sq;

	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++)
	{
	    scanf("%d%d",&a,&b);
	    if(a>b)
	    {
		tmp=a;
		a=b;
		b=tmp;
	    }

	    for(i=a,count=0;i<=b;i++)
	    {
		sq=sqrt((double)i);
	//	if(sq-(int)sq!=0.0) continue;
	//	printf("sq %d\n",i);
	
		tmp=i;
		k=0;
		while(tmp>0)
		{	
			num[k++]=tmp%10;
			tmp/=10;
		}
		num[k]='\0';
		
		for(j=0;j<=k/2;j++)
		{
		   if(num[j]!=num[k-j-1]) break;
		}
		if(j!=(k/2)+1) continue;

		sq=sqrt((double)i);
		if(sq-(int)sq!=0.0) continue;
		
		tmp=(int)sq;
		k=0;
		while(tmp>0)
		{
			num[k++]=tmp%10;
			tmp/=10;
		}
		num[k]='\0';
		
		for(j=0;j<=k/2;j++)
			if(num[j]!=num[k-j-1]) break;
		if(j==(k/2)+1) count++;
		
            }
	   printf("Case #%d: %d\n",cas,count);
	}
	return 0;
	
}
