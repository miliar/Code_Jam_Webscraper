/*
TASK: Ticket Swapping
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
typedef pair<int,int> PII;
typedef long long LL;

int N,M,T;
long long s[2005][2005];
long long p[2005];
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        tt++;
        scanf("%d%d",&N,&M);
        int x,y,z;
        vector<pair<pair<int,int>,int> > v;
        map<int,long long> mp;
        map<int,long long>::iterator it;
        long long cur=0,new_sum=0,tic,cost;
        for(i=0;i<M;i++)
        {
            scanf("%d%d%d",&x,&y,&z);
//            ed[y]+=z;
//            st[x]+=z;
            mp[x]+=z;
            mp[y]-=z;
            k=y-x;
            cur+=((long long)(k)*N-(((long long)k*k-k)/2))*(long long)z;
//            cout << cur << endl;
            //v.push_back(make_pair(make_pair(x,y),z));
        }
        i=0;
        for(it=mp.begin();it!=mp.end();it++)
        {
            i++;
            x=(*it).X;
            y=(*it).Y;
            p[i]=x;
            if(y>0)
            {
                for(j=1;j<=2000;j++)
                    s[j][i]+=s[j][i-1];
                s[i][i]+=y;
            }
            else
            {
                k=0;    y=-y;
                for(j=2000;j>=1;j--)
                {
                    y-=s[j][i-1];
                    if(y<0) s[j][i]=-y,y=0;
                    else    s[j][i]=0;
                }
            }
        }
        long long a,b,c;
        for(i=1;i<=2000;i++)
        {
            a=0;
            for(j=2000-1;j>=i;j--)
            {
                c=p[j+1]-p[i];
                s[i][j]-=a;
                b=s[i][j];
                new_sum+=((c)*N-(((long long)c*c-c)/2))*(long long)b;;
                a+=b;
            }
        }
        memset(s,0,sizeof s);
//        printf("%I64d %I64d\n",cur,new_sum);
        printf("Case #%d: %I64d\n",tt,cur-new_sum);
    }
}
