#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>
#include <vector>
#include <cmath>
#include <string.h>
#include <time.h>
#include <fstream>
#include <set>
#include <stack>
#include <list>

using namespace std;

#define READ freopen("acm.in","r",stdin)
#define WRITE freopen("acm.out","w",stdout)
#define ll long long
#define ull unsigned long long 
#define uint unsigned int
#define PII pair<int,int>
#define PDD pair<double,double>
#define fst first
#define sec second
#define MS(x,d) memset(x,d,sizeof(x))
#define INF 0x3f3f3f3f
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MOD 1000000007
#define MAX 1111



int main()
{
    READ;
    int cas;
    cin>>cas;
    WRITE;
    for(int T=1;T<=cas;T++)
    {
        double C,F,X;
        cin>>C>>F>>X;
        double left=X;
        double now=0.0;
        double rate=2.0;
        if(C>X)
        {
            printf("Case #%d: %f\n",T,X/2.0);
            continue;
        }
        while(1)
        {
            double buy=(left)/(F+rate);
            double nBuy=(left-C)/rate;
            if(buy<nBuy)
                now+=C/rate,rate+=F;
            else
            {
                now+=left/rate;
                break;
            }
            if(left<1e-9)
                break;
        }
        printf("Case #%d: %f\n",T,now);
    } 
    return 0;
}