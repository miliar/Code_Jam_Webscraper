#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    double c,f,x,res,res1,res2,res3,freq;
    int t,test;
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    cin >>test;
    t=1;
    while(t<=test)
    {
        res=0.0;
        res3=0.0;
        res1=2.0;
        res2=1.0;
        cin >> c >> f >> x;
        freq=2.0;
        while(res2<res1)
        {
            res=res+res3;
            res1=x/freq;
            res3=c/freq;
            res2=x/(freq+f);
            res2=res2+res3;
            freq=freq+f;
        }
        res=res+res1;
        printf("Case #%d: %.7llf\n",t,res);
        t++;
    }
    return 0;
}
