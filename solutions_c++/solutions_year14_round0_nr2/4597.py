#include<cstdio>
#include<iostream>
  using namespace std;
  int main()
{
  int tn,j,k,n;
  double C,F,X,min,i,ans;
  scanf("%d",&tn);
  for(k=1;k<=tn;k++)
  {
   scanf("%lf %lf %lf",&C,&F,&X);
   n=static_cast<int>((F*X-2*C)/(F*C));
   if(n<0)
   n=0;
   for(i=0,ans=0;i<n;i++)
   {
     ans=ans+C/(2+F*i);
   }
   ans=ans+X/(F*n+2);
   printf("Case #%d: %f\n",k,ans);
  }
  return 0;
}

