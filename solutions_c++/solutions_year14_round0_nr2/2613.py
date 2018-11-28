#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <algorithm>
#define maxn 10010
#define maxx_N 26
#define INF 0x7fffffff
#define eps 1e-6

using namespace std;
struct contestant{
    long long ti,di;
    char name[30];
    bool operator <(const contestant &a)const
    {
        if(a.ti!=ti)
            return a.ti > ti;
        return strcmp(a.name,name)>0;
    }
}ss[maxn];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas,test=1;
    scanf("%d",&cas);
    while(cas--){
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double minu = x / 2.0;int i = 0;
        while(true){
            double res = minu-x/(2.0+i*f)+c/(2.0+i*f)+x/(2.0+(i+1.0)*f);
            i++;
            if(res<minu)minu=res;
            else break;
        }
        printf("Case #%d: %.7lf\n",test++,minu);
    }
    return 0;
}
