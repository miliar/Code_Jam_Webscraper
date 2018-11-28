// OUM NAMA MA SWARASATI

#include"math.h"
#include"stdio.h"
#include"string.h"
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include"stdlib.h"
#include<algorithm>
#include"iostream"
#define sf(p) scanf("%d",&p)
#define s2(p,q) scanf("d",&p,&q)
#define fr(p,q,r) for(int i=p;i<=q;i+=r)
#define fs(p,q,r,a) for(int i=p;i<q;sf(a[i]),i+=r)
#define sc(c) scanf("%c",&c)
#define pf(p) printf("%d\n",p)
#define pl(p) printf("%lld\n",p)
#define pn(p) printf("%d",p)

#define mn(p,q) p<q?p:q
#define mx(p,q) p>=q?p:q

using namespace std;
typedef long long int ll;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("pb.txt","w",stdout);
    int t,T;
    double c,f,X,i,a,b,p;
    sf(t),T=t;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&X);
        i=2.0;
        a=X/i;
        b=c/i;
        p=b;
        b+=X/(i+f);
        while(b<a)
        {
            a=b;
            b=p;
            i=i+f;
            b+=c/i;
            p=b;
            b+=(X/(i+f));
        }
        printf("Case #%d: %0.7lf\n",T-t,a);
    }
    return 0;
}


