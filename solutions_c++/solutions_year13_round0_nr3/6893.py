#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;
int main()
{	int t,k,a,b,count;
	FILE *fp;
	if((fp=fopen("/Users/rohitat/C/codejam/C-small-attempt0.in","r"))==NULL)
	{	printf("BULLSHIT");
		exit(0);
	}
	fscanf(fp,"%d",&t);
	for(k=1;k<=t;k++)
	{	fscanf(fp,"%d",&a);
		fscanf(fp,"%d",&b);
		count=0;
		for(int i=a;i<=b;i++)
		{
			if(sqrt(i)==(int)sqrt(i))
			{	int rev,num,dig;
				rev = 0;
				num=i;
 				while (num > 0)
 				{
      					dig = num % 10;
      					rev = rev * 10 + dig;
      					num = num / 10;
				}	
				if(i==rev)
				{	rev=0;
					num=sqrt(i);
                                 	while (num > 0)
                                  	{
 	                                	dig = num % 10;
                                        	rev = rev * 10 + dig;
                                          	num = num / 10;
                                  	}
					if(rev==sqrt(i))
					{	count++;	
					}
				}
			}
				
		}
		printf("Case #%d: %d\n",k,count);
	}	
	fclose(fp);
	return 0;
}
