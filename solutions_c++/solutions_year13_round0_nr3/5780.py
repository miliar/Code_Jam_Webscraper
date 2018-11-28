#include<stdio.h>
#define size 4
int chk_palin(int a)
{
    if(a==1000)return 0;
    if(a<=10)return 1;
    if(a<100)
    {
        if(a/10==a%10)return 1;
        else return 0;
    }
    else
    {
      if(a/100==a%10)return 1;
      else return 0;
    }
    //int len=strlen()
}
int main()
{
	int t,i,j,k,flag,n,m,p=0,a[1000],ct=1;
	j=0;
	for(i=1;i<1001;i++)
	{
	    if(chk_palin(i)&&chk_palin(i*i))
	    {
	        a[j++]=i*i;
	        //printf("%d\n",i*i);
	    }
	}
	scanf("%d",&t);
	while(t--)
	{
	    p=0;
        scanf("%d %d",&n,&m);
        for(i=0;i<j;i++)
        {
            if(a[i]<=m)
            {
                if(a[i]>=n)p++;
            }
            else break;
        }
        printf("Case #%d: %d\n",ct++,p);
	}
	return 0;
}
