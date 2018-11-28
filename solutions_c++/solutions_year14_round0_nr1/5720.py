#include<cstdio>
#define LOCAL

int main()
{
#ifdef LOCAL
	freopen("A-small-attempt2.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
  int t,i,j;
  int a[4][4];
  int  b[4][4];
  int c[4];
  int d[4];
  int final,ans1,ans2,count,count2;
   count2=1;
   scanf("%d",&t );
   while(t--)
   {   
	   count=0;
	  
	   scanf("%d",&ans1);
	   for(i=0;i<4;i++)
		   for(j=0;j<4;j++)
		   {scanf("%d",&a[i][j]);}
	   scanf("%d",&ans2);
	   for(i=0;i<4;i++)
		   for(j=0;j<4;j++)
		   {scanf("%d",&b[i][j]);}
	   for(i=0;i<4;i++)
			   c[i]=a[ans1-1][i];
	   for(i=0;i<4;i++)
			   d[i]=b[ans2-1][i];
	  /*  for(i=0;i<4;i++)
			printf(" %d",c[i]);
		 for(i=0;i<4;i++)
			printf(" %d",d[i]);
		 	printf("\n");*/
	   for(i=0;i<4;i++)
		  for(j=0;j<4;j++)
             if(c[i]-d[j]==0)
			  {
				  count++;
			     final=c[i];
			    //
				 //printf("%d %d %d",i,j,c[j]);
				 break;
			  }
	  if(count==0)printf("Case #%d: Volunteer cheated!\n",count2);
	  if(count==1)printf("Case #%d: %d\n",count2,final);
	  if(count>1)printf("Case #%d: Bad magician!\n",count2);
	  count2++;
   }
  
  return 0;

}
