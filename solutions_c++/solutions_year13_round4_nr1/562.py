#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#define MOD 1000002013
using namespace std;

map<int,long long> MO,ME;
int n,m;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i,j,o,e;
    long long p,s1,s2;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        MO.clear();
        ME.clear();
        scanf("%d %d",&n,&m);
        s1=0;
        for(i=0;i<m;i++)
        {
            scanf("%d %d %I64d",&o,&e,&p);
            MO[o]=MO[o]+p;
            ME[e]=ME[e]+p;
            s1=(s1+((n*2LL-e+o+1)*(e-o)/2LL%MOD)*(p%MOD))%MOD;
        }
        s2=0;
        for(map<int,long long>::reverse_iterator it1=MO.rbegin();it1!=MO.rend();it1++)
        {
            while(it1->second!=0)
            {
                map<int,long long>::iterator it2=ME.lower_bound(it1->first);
                o=it1->first;
                e=it2->first;
                p=min(it1->second,it2->second);
                s2=(s2+((n*2LL-e+o+1)*(e-o)/2LL%MOD)*(p%MOD))%MOD;
                it1->second=it1->second-p;
                it2->second=it2->second-p;
                if(it2->second==0)
                {
                    ME.erase(it2);
                }
            }
        }
        printf("Case #%d: %I64d\n",c+1,(s1-s2+MOD)%MOD);
    }
    return 0;
}
