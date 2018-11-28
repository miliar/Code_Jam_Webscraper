#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;
typedef long long ll;

#define FR(i,en) for(int i=0; i<(int)(en); i++)
#define FOR(i,st,en) for(int i=(st); i<(int)(en); i++)

int main()
{
    int t,i;
    double c,f,x;
    double res, p1, p2;
    scanf("%d",&t);
    FR (test_cases,t) {
        printf("Case #%d: ",test_cases+1);
        scanf("%lf%lf%lf",&c,&f,&x);
        p1=(double)x/2;
        p2=0.0;
        res=999999.0;
        i=0;
        while (p1+p2<res) {
            res=p1+p2;
            i++;
            p1=(double)x/((i*f)+2);
            p2+=(double)c/(((i-1)*f)+2);
        }
        printf("%.7lf\n",res);
    }
    return 0;
}
