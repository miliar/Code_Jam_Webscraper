#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long int int64;
int64 a[1000001];
int main()
{
          freopen("in.txt","r",stdin);
          freopen("out.txt","w",stdout);
          int64 i,j,k,m,n=0,t,ans;
          double C,F,X,T,R;
          scanf("%lld",&t);
          while(t--)
                    {
                    T = 0;
                    R = 2;
                    n++;
                     scanf("%lf %lf %lf",&C,&F,&X);
                     k=0;
                     while(k==0){
                                 if((X/R)<(C/R+X/(R+F)))
                                                     {
                                                     T+=X/R;
                                                     k=1;
                                                     }
                                 else
                                     {
                                     T+=C/R;
                                     R+=F;
                                     }
                                 }
                     printf("Case #%lld: %0.7lf\n",n,T);
                     }
                 
 //system("pause");
}
