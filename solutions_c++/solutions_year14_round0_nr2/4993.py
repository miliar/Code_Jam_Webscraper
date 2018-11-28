#include <iostream>
#include<cstdio>

using namespace std;

int main()
{
   int z,T;
   cin>>T;
   for(z=1;z<=T;z++)
   {
    int cnt=1;
    double c,f,x,s=0,tmp,rate,old,prev;
    cin>>c>>f>>x;

    rate=2;
    prev=0;
    old = x/2;
 
    if(x<=c)
    {
    printf("Case #%d: %0.7f\n",z,x/rate);
    }
    else
    {
    while(1)
    {
    s=prev;
    s+=c/rate;
    prev=s;
    rate+=f;
    s+=x/rate;
    if(s>old)
    break;
    else
    old=s;
    }
    printf("Case #%d: %0.7f\n",z,old);
    }
   }
   return 0;
}

