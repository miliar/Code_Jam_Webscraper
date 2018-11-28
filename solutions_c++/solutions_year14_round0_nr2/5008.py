#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
const double eps=1e-9;
typedef long long ll;
const int maxn=5;
double C,F,X;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int tcase=0;
    scanf("%d",&t);
    while(t--)
    {
        tcase++;
        printf("Case #%d: ",tcase);
        scanf("%lf%lf%lf",&C,&F,&X);
        double sp=2;
        double finish=X/sp;
        double now=0;
        while(finish-(now+C/sp+X/(sp+F))>eps)
        {
            finish=now+C/sp+X/(sp+F);
            now+=C/sp;
            sp+=F;
        }
        printf("%.7lf\n",finish);
    }
    return 0;
}
