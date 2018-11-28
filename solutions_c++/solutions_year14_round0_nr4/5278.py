#include<cstdio>
#include<algorithm>
using namespace std;
int t,n,i,j,k,r;
int c[10],sum2,cur,sum1,count1=1;
double a[10],b[10],d[10];
#define LOCAL
void BubbleSort (double V[], int n)
{
 int i,j;
 double t;
 for (i = 1; i<n; i++) {
  for (j=0; j<n-i; j++) {
   if (V[j]>V[j+1]) {
    t=V[j];
    V[j]=V[j+1];
    V[j+1]=t;
   }
  }
 }
}
int main()
{
#ifdef LOCAL
	freopen("D-small-attempt1.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
 
   scanf("%d",&t );
   while(t--)
   {   
	  sum1=0;
	   sum2=0;
	   scanf("%d",&n);
	    for(i=0;i<n;i++)
		  c[i]=1;
	   for(i=0;i<n;i++) scanf("%lf",&a[i]);
	   for(i=0;i<n;i++)scanf("%lf",&b[i]);
	   BubbleSort(a,n);
	   BubbleSort(b,n);
	     //for(j=0;j<n;j++)printf("%lf",a[j]);printf("\n");
		  //for(j=0;j<n;j++)printf("%lf",b[j]);printf("\n");
	   i=0;
	   cur=0;
	   //for(j=0;j<n;j++)printf("%d",c[j]);
       i=0;
	   while(cur<n)
	   {
		   if(b[cur]>a[i]) 
		   {
			   c[i]=0;cur++;i++;
			   //printf("*");   
		      // for(j=0;j<n;j++)printf("%d",c[j]);printf("\n");
		   }
		   else 
		   {
			   cur++;
			   //for(j=0;j<n;j++)
				  // printf("%d",c[j]);
			   //printf("\n");
		   }
	   }
	   for(i=0;i<n;i++)
		   sum2=sum2+c[i];
	   //printf("%d\n",sum2);
	    for(i=0;i<n;i++)
		  d[i]=0;
	   i=0;r=0;
	   j=n-1;k=n-1;
	   while((a[i]<b[r])&&(i<n)&&(r<n))
	   {
		   i++;j--;
	   }
            
	   while((k>=i)&&(j>=r))
	   if(a[k]>b[j])
	   {d[k]=1;k--;j--;}
	   else{i++;j--;}
	    for(i=0;i<n;i++)
		   sum1=sum1+d[i];
	     
	   // printf("%d\n",sum1);
	printf("Case #%d: %d %d\n", count1,sum1,sum2);	

    count1++;
	  
   }
  
  return 0;

}
