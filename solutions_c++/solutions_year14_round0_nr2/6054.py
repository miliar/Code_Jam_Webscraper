#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <set>
#include <queue>

using namespace std;
#define i64 long long

#define INF 999999999

int a[4][4],b[4][4];
int x,y;
map<int,int> mp;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    //freopen("B-large.in.txt","r",stdin);

    int i,j,cases,k,cs;
    double c,f,x,gmin,cf,t1,tot,t2,t3,tot2;

    scanf("%d",&cases);
    for(cs=1;cs<=cases;++cs)
    {
        gmin=INF;
        cf=2;
        tot=0;
        tot2=0;
        t1=t2=t3=0;
        scanf("%lf %lf %lf",&c,&f,&x);

        while(true)
        {
            t1=x/cf;
            t2=c/cf;
            t3=tot+t2;

            tot2=tot+t1;
            tot=t3;

            if(tot2<gmin)
            {
                gmin=tot2;
            }
            cf+=f;

            if((t3)>=gmin)
            {
                break;
            }
        }

        printf("Case #%d: %.7lf\n",cs,gmin);
    }

    return 0;
}

