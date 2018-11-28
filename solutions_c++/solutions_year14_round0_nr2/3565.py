#include <iostream>
#include <cstdio>
using namespace std;

const int MAXR = 100000;
int T,t;
double C,F,X;
double m,ans,r,t1,t2;

struct Record
{
    double time;
    double rate;
    double ans;
};

Record rs[MAXR];

int main()
{
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>C>>F>>X;
        
        // max farm to buy
        int mf = X/C;
        
        rs[0].time = 0;
        rs[0].rate = 2.0;
        rs[0].ans = X/rs[0].rate;
        
        ans = rs[0].ans;
        
        for(int i=1;i<MAXR;i++)
        {
            rs[i].time = rs[i-1].time + C/rs[i-1].rate;
            rs[i].rate = rs[i-1].rate + F;
            rs[i].ans = rs[i].time + X/rs[i].rate;
            
            if(rs[i].ans < ans)
            {
                ans = rs[i].ans;
            }
            else
            {
                break;
            }
        }
        
        printf("Case #%d: %0.7lf\n", t, ans);
    }    
    return 0;
}