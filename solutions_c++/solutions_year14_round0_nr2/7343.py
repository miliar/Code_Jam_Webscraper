#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
/*In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie.
Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm,
it costs you C cookies and gives you an extra F cookies per second.
Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy.*/
int main()
{
    //freopen("2in.txt", "r", stdin);
    int T;
    cin>>T;
    double C,F,X;//C-cookie farm price,F-extra cookie per sec,X-winning cookie
    double v=2;//current cookie gaining speed
    double c=0;//current cookie
    double t=0;//time taken
    double tb=0,ta=0;//time remaining to produce winning cookie before and after getting farm
    double tf=0;//time taken to get enough cookie for farm
    bool b=true;//whether to buy farm or not
    for (int i=0;i<T;i++)
    {
        cin>>C>>F>>X;//C-cookie farm price,F-extra cookie per sec,X-winning cookie
        while(b)
        {
            tb=X/v;//no cookie for farm yet
            ta=X/(v+F);//assuming got cookie for farm alr
            tf=C/v;
            if(tb>ta+tf)
            {
                b=true;
                t+=tf;
                v+=F;
            }
            else
            {
                b=false;
                t+=tb;
                c+=(v*tb);
            }
        }
        printf("Case #%d: %.7f\n",i+1,t);
        c=0,t=0,b=true,v=2;
    }
}

