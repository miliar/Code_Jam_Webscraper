#include<iostream>
#include<cstdio>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<sstream>
#include<bitset>
#include<set>
#include<cstring>
#include<string>
#include<utility>
#define pi 3.14159
using namespace std;
int main()
{

//freopen("A-small-attempt2.in","r",stdin);
   //freopen("A_5.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);

   while(T--)
    {
        long r,t,k1;
        int c1=2;
        bool bl=true;
        scanf("%ld %ld",&r,&t);
        t=t*1000000;
        double a,b,c,d1=0.0,k;
        a=pi*(r*r);long int co=0;
        while(bl)
        {
            r+=1;
            b=pi*(r*r);
            c=b-a;
            a=b;
            c/=pi;

            if(c1%2==0)
            {
                d1+=c;
                k=d1*1000000;
                k1=k;
           if(k1<=t)
           {

               co++;
           }
           }
           c1++;
           if(k1>t) bl=false;
        }
        printf("Case #%d: %ld\n",++cas,co);
}
    return 0;
}
