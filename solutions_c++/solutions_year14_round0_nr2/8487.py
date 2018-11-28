#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
    double c,f,x,currf,tm,tm1,y;
    int t,k,count;
    //cin>>t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        //cin>>c>>f>>x;
        scanf("%lf%lf%lf",&c,&f,&x);
        currf=2;
        tm=x/currf;
        y=0;
        count=0;
        do
        {
            if(count!=0)
            tm=tm1;
            y=y+c/currf;
            currf=currf+f;
            //if(tm>(y+x/currf))
            //tm=y+x/currf;
            count++;
            tm1=y+x/currf;
        }while(tm1<tm);
        printf("Case #%d: ",k);
        printf("%.7lf\n",tm);
             
    }    
return 0;
}
