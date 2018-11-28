#include<stdio.h>
main()
{
  int t,k,c,s;
  int i;
  int j;
  int chunk;
  FILE *fp=fopen("abc","r");
  fscanf(fp,"%d",&t);
  for(i=1;i<=t;i++)
  {
    fscanf(fp,"%d",&k);
    fscanf(fp,"%d",&c);
    fscanf(fp,"%d",&s);

    if(k==1)
    {
       if(s==0)
         printf("Case #%d: IMPOSSIBLE\n",i);
       else
         printf("Case #%d: 1\n",i);

       continue;
    }

    if(c==1)
    {
      if(s<k)
         printf("Case #%d: IMPOSSIBLE\n",i);
      else
      {
         int m;
         printf("Case #%d: ",i);
	 for(m=1;m<=k;m++)
	 {
	   if(m==k)
	   {
             printf("%d\n",m);
	   }
	   else
	   {
             printf("%d ",m);
	   }
	 }
      }

      continue;

    }
    else
    {
       if(s < k-1)
       {
         printf("Case #%d: IMPOSSIBLE\n",i);
	 continue;
       }
    }

    chunk=0;
    printf("Case #%d: ",i);
    for(j=2;j<=k;j++)
    {
       if(j==k)
       {
         printf("%d\n",j+chunk);
       }
       else
       {
         printf("%d ",j+chunk);
       }
       chunk=chunk+k;
    }
  }
}
