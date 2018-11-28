#include<cstdio>
#define LOCAL
int main()
{
#ifdef LOCAL
	freopen("B-small-attempt4.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
	int t,i,k;
	int count=1;
	double c,f,x,ans;
   scanf("%d",&t );
   while(t--)
   {   
	   ans=0;
	   scanf("%lf%lf%lf",&c,&f,&x);
	   if(c>=x)
	   {
		   ans=x/2;
	      printf("Case #%d: %.7lf\n",count,ans);
	      count++;
	   }
	   if(c<x)
	   {
           for(k=0;k<30000;k++)
		   {
			   if(c/((k*f)+2)+x/((k+1)*f+2)>x/(k*f+2))
				   break;
		   }
		   //printf(" %d",k);
		   for(i=0;i<k;i++)
		   {
			   ans=ans+c/(i*f+2); //printf(" %lf",ans);
		   }
		   ans=ans+x/(k*f+2);
		   printf("Case #%d: %.7lf\n",count,ans);
		   count++;
	   }
   }
  
  return 0;

}
