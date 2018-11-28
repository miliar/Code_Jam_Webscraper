#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int T,t;
double cost,more,win;

double cal(int x)
{
    double get=2,res=0;
    while(x)
    {
        res+=cost/get;
        x--;
        get+=more;
    }
    res+=win/get;
    return res;
}

int main()
{
    int i;
    double tmp,ans;
    freopen("Bin.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&cost,&more,&win);
        ans=win/2;
        for(i=1;;i++)
        {
            tmp=cal(i);
            if(tmp>=ans) break;
            ans=tmp;
        }
        printf("Case #%d: %.7f\n",t,ans);
    }
    return 0;
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
*/
