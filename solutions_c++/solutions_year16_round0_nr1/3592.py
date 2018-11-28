#include<stdio.h>
#include<string.h>
#define TRUE 1
#define FALSE 0
main()
{
  int t;
  FILE *fp=fopen("abc","r");
  int i,j,k;
  int n,temp,x;
  int found,count;
  int a[10];
  fscanf(fp,"%d",&t);
  for(i=1;i<=t;i++)
  {
    fscanf(fp,"%d",&n);
    if(n==0)
    {
         printf("Case #%d: INSOMNIA\n",i);
	 continue;
    }

    memset(a,0,sizeof(int)*10);
    found=FALSE;

    j=1;

//    for(j=1;j<=45;j++)
    while(1)
    {
       count=0;
       x=n*j;
       temp=x;
       while(x)
       {
         if(a[x%10]==0)
	    a[x%10]=1;

	 x=x/10;
       }
       for(k=0;k<10;k++)
       {
         if(a[k]==1)
	   count++;
       }
       if(count==10)
       {
         printf("Case #%d: %d\n",i,temp);
	 found = TRUE;
	 break;
       }
       j++;
    }

    if(found == FALSE)
         printf("Case #%d: INSOMNIA\n",i);
  }
}
