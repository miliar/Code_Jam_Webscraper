#include<cstdio>
#include<algorithm>
#include<cstring>
main()
{
 int t,a[20],b[5][5],i,j,x,c,k,m,y;     
  scanf("%d",&t);
  for(k=1;k<=t;k++)
  {
   memset(a,0,sizeof(a));   
   c=0;      
   scanf("%d",&x);
   for(i=1;i<=4;i++)
   {           
    for(j=1;j<=4;j++)
    {         
       scanf("%d",&b[i][j]);
       if(i==x)
        a[b[i][j]]=1;
    } 
   }  
   
   scanf("%d",&y);
   for(i=1;i<=4;i++)
   {           
    for(j=1;j<=4;j++)
    {         
       scanf("%d",&b[i][j]);
       if(i==y&&a[b[i][j]]==1)
       {
        c++;
        m=b[i][j];
       }
    } 
   }  
         
     if(c==1)
      printf("Case #%d: %d\n",k,m);
      
      if(c>1)
       printf("Case #%d: Bad magician!\n",k);
       
       if(c==0)
        printf("Case #%d: Volunteer cheated!\n",k);    
         
  }    
      
return 0;      
}
