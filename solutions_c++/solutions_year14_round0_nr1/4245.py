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
    freopen("A-small-attempt2.in","r",stdin);
    freopen("pa.txt","w",stdout);
    int t,T,fa,sa,r[5],R[5],j,k,cnt,y,a,b,c,d;
    sf(t),T=t;
    while(t--)
    {
        sf(fa);
        fr(1,4,1)
        {
            scanf("%d%d%d%d",&a,&b,&c,&d);
            if(i==fa)
                r[1]=a,r[2]=b,r[3]=c,r[4]=d;
        }
        sf(sa);
        cnt=0;
        fr(1,4,1)
        {
            scanf("%d%d%d%d",&R[1],&R[2],&R[3],&R[4]);
            if(i==sa)
            {
                for(j=1;j<=4;j++)
                {
                    for(k=1;k<=4;k++)
                    {
                        if(r[j]==R[k])
                            cnt++,y=r[j];
                    }
                }
            }
        }
        if(!cnt)
            printf("Case #%d: Volunteer cheated!\n",T-t);
        else if(cnt==1)
            printf("Case #%d: %d\n",T-t,y);
        else
            printf("Case #%d: Bad magician!\n",T-t);
    }
    return 0;
}








