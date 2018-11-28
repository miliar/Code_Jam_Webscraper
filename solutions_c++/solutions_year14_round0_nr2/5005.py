#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
const double eps=1e-9;
typedef long long ll;
const int maxn=5;
double c,f,x;
int main()
{
    freopen("B-large.in","r",stdin);
//    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tt;
    int ct=0;
    scanf("%d",&tt);
    while(tt--)
    {
        ct++;
        printf("Case #%d: ",ct);
        scanf("%lf%lf%lf",&c,&f,&x);
        double sp=2;
        double finish=x/sp;
        double now=0;
        while(finish-(now+c/sp+x/(sp+f))>eps)
        {
            finish=now+c/sp+x/(sp+f);
            now+=c/sp;
            sp+=f;
        }
        printf("%.7lf\n",finish);
    }
    return 0;
}
