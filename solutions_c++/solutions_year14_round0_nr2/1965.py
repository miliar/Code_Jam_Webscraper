#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string.h>
#include<cstdlib>

using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


int min(int a,int b)
{
        return a<b?a:b;
}


int max(int a,int b)
{
        return a>b?a:b;
}

int main()
{
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\a.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\b.out","w",stdout);
        int t,i,j,n,m,k;
        double a,b,c,f,x,p,y;
        int ar[10][10];
        int br[10][10];
        scanf("%d",&t);
        k=t;
        while(t--)
        {
                scanf("%lf",&c);
                scanf("%lf",&f);
                scanf("%lf",&x);
                a=2;
                y=0;
                while(x/(a*1.0)> ((c/(a*1.0)) + x/((a+f)*1.0)))
                {
                        y=y+c/(a*1.0);
                        a=a+f;
                }
                y=y+x/(a*1.0);


                        printf("Case #%d: %0.7lf\n",k-t,y);

        }
        return 0;
}
