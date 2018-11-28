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
#define s3(p,q,r) scanf("%d%d%d",&p,&q,&r)
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
    freopen("D-large.in","r",stdin);
    freopen("pd.txt","w",stdout);
    int t,T,n,i,j,cntN,cntK;
    double N[1005],K[1005];
    int visN[1005],visK[1005];
    sf(t),T=t;
    while(t--)
    {
        sf(n);

        for(i=0;i<n;i++)
            scanf("%lf",&N[i]),visN[i]=0;
        sort(N,N+n);
        for(i=0;i<n;i++)
            scanf("%lf",&K[i]),visK[i]=0;
        sort(K,K+n);

        for(i=cntN=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(!visN[i]&&!visK[j])
                {
                    if(N[i]>K[j])
                    {
                        cntN++;
                        visN[i]=visK[j]=1;
                    }
                }
            }
        }
        for(i=0;i<n;i++)
            visN[i]=visK[i]=0;
        for(i=cntK=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(!visN[i]&&!visK[j])
                {
                    if(K[i]>N[j])
                    {
                        cntK++;
                        visN[i]=visK[j]=1;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",T-t,cntN,n-cntK);
    }
    return 0;
}

