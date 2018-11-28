#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <map>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <functional>
#include <sstream>
#include <list>
#include <complex>

#define maxlongint 2147483647
#define biglongint 2139062143
#define LL long long
#define ULL unsigned long long
#define p_b push_back
#define m_p make_pair
#define l_b lower_bound
#define w1 first
#define w2 second

using namespace std;

typedef pair<int,int> PII;
typedef pair<pair<int,int>,int> PIII;
typedef pair<pair<int,int>,pair<int,int> > PIIII;
typedef pair<double,double> PDD;
typedef pair<double,int> PDI;
typedef pair<string,int> PSI;
typedef pair<pair<double,double>,double> PDDD;
typedef pair<pair<double,double>,pair<double,double> > PDDDD;

int tt,m,n,ok,flag,sj;
int f[30][30],b[30];
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&tt);
    for (int gb=1;gb<=tt;gb++)
    {
        scanf("%d %d",&m,&n);
        memset(f,0,sizeof(f));
        for (int i=1;i<=m;i++)
            for (int j=1;j<=n;j++)
                scanf("%d",&f[i][j]);
        for (int i=0;i<=m+n;i++) b[i]=1;
        ok=0;
        while (b[0]==1)
        {
            flag=1;
            for (int i=1;i<=m;i++)
            {
                for (int j=1;j<=n;j++)
                    if (f[i][j]!=min(b[i],b[m+j]))
                    {
                        flag=0;
                        break;
                    }
                if (flag==0) break;
            }
            if (flag==1)
            {
                ok=1;
                break;
            }
            sj=m+n;
            while (b[sj]==2)
            {
                b[sj]=1;
                --sj;
            }
            ++b[sj];
        }
        cout<<"Case #"<<gb<<": ";
        if (ok==0) cout<<"NO"<<endl; else cout<<"YES"<<endl;
    }

    return 0;
}
