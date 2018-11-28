#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int paintvol(int r)
{
    return 2*r-1;
}
int cal(int &r,int &t)
{
    int vol;
    int ring=0;
    for (int rad=r+1;;rad+=2)
    {
        vol=paintvol(rad);
        if (vol>t) break;
        else
        {
            t-=vol;
            ring++;
        }
    }
    return ring;
}
int main()
{
    int T;
    cin>>T;
    int r,t;
    int a;
    for(int te=1;te<=T;te++)
    {
        cin>>r>>t;
        a=cal(r,t);
        printf("Case #%d: %d\n",te,a);
    }
}
