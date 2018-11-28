#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
bool chkp(int a)
{
    int count=0;
    int tmp=a;
    while(tmp!=0)
    {
        count++;
        tmp/=10;
        //printf("tmp = %d %d\n",tmp,count);
    }
    //int stack[count/2];
    //int index=0;
    for(int i=0;i<count/2;i++)
    {
        if(a%(int)pow(10,i+1)!=a/(int)pow(10,count-i-1))return 0;
    }
    return 1;
}
bool chksq(int a)
{
    int b=(int)sqrt(a);
    //printf("%d\n",b);
    if(a!=b*b)return 0;
    else
    {
        //printf("%d %d\n",a,b);
        if(!chkp(b))return 0;
        return 1;
    }
}
main()
{
	int n;
	scanf("%d",&n);
	for(int k=1;k<=n;k++)
	{
		int a,b,count=0;
		scanf("%d %d",&a,&b);
		for(int i=a;i<=b;i++)
		{
		    if(!chksq(i))continue;
		    if(!chkp(i))continue;
		    count++;
		}
		printf("Case #%d: ",k);
		printf("%d\n",count);
	}
}
