#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<queue>
#include<cmath>

#define For(i,n) for(int i=0;i<(n);i++)
#define Fori(i,si,n) for( int i=(si);i<(n);i++)
#define clr(x,y)    memset(x,y,sizeof(x))
#define sf  scanf
#define pf  printf
#define mp  make_pair

using namespace std;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas;    cin>>cas;
    int _=1;
    while(cas--)
    {
        double X,F,C;
        sf("%lf%lf%lf",&C,&F,&X);
        {
            double curRate = 2.0,cost=0;
            while(true){
                double nt = X/curRate;
                double nt1 = C/curRate + X/(curRate+F);
                if(nt < nt1)
                    break;
                else
                {
                    cost += C/curRate;
                    curRate = curRate+F;
                }
            }
            pf("Case #%d: %.7lf\n",_++,cost+X/curRate);
        }
    }
    return 0;
}

