#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;

const int mod=1000002013;

pair<pair<long long,int>,long long> b[2020];
pair<long long,long long> s[2020];


int main()
{
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        memset(b,0,sizeof(b));
        int n,m;
        scanf("%d%d",&n,&m);
        long long ans=0;
        for (int i=0;i<m;i++)
        {
            int o,e,p;
            scanf("%d%d%d",&o,&e,&p);
            long long tmp=(n+n-(e-o)+1)*(e-o)/2;
            tmp%=mod;
            //printf("!%d\n",tmp);
            ans+=tmp*p;
            ans%=mod;
            //printf("!!!%d %d %d\n",o,e,p);
            b[2*i].first.first=o;
            b[2*i].first.second=0;
            b[2*i].second=p;
            b[2*i+1].first.first=e;
            b[2*i+1].first.second=1;
            b[2*i+1].second=p;
            //printf("%d: %I64d %d %I64d\n",2*i,b[2*i].first.first,b[2*i].first.second,b[2*i].second);
            //printf("%d: %I64d %d %I64d\n",2*i+1,b[2*i+1].first.first,b[2*i+1].first.second,b[2*i+1].second);
        }
        //ans=0;
        sort(b,b+2*m);
        //for (int i=0;i<2*m;i++)
        //    printf("%I64d %d %I64d\n",b[i].first.first,b[i].first.second,b[i].second);
        memset(s,0,sizeof(s));
        int size=0;
        for (int i=0;i<2*m;i++)
        {
            if (b[i].first.second==0)
            {
                s[size].first=b[i].first.first;
                s[size].second=b[i].second;
                size++;
            }
            else
            {
                while (b[i].second)
                {
                    long long o,e,p;
                    o=s[size-1].first;
                    e=b[i].first.first;
                    if (b[i].second>=s[size-1].second)
                    {
                        p=s[size-1].second;
                        size--;
                    }
                    else p=b[i].second;
                    long long tmp=(n+n-(e-o)+1)*(e-o)/2;
                    tmp%=mod;
                    ans-=tmp*p;
                    ans+=mod;
                    ans%=mod;
                    b[i].second-=p;
                }
            }
            //printf("Ans: %d\n",(int)ans);
            //for (int i=0;i<size;i++)
            //{
            //    cout<<s[i].first<<" "<<s[i].second<<endl;
            //}
        }
        printf("Case #%d: %d\n",t,(int)ans);
    }
    return 0;
}
