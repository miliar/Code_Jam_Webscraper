/*
TASK: Falling Diamonds [small]
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
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
typedef pair<int,int> PII;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    int a,b,q,p;
    map<pair<int,pair<int,int> >,double> ss;
    while(T--)
    {
        tt++;
        int x,y;
        scanf("%d%d%d",&N,&x,&y);
        if(abs(x)+abs(y)>10)
        {
            int co=0;
            printf("Case #%d: %lf\n",tt,co*2.0/(1<<N));
            continue;
        }
//        if(mp[make_pair(N,make_pair(x,y))])
        int co=0;
        for(i=0;i<(1<<N-1);i++)
        {
            map<pair<int,int>,bool> mp;
            mp[make_pair(0,0)]=1;
            for(j=1;j<(1<<N-1);j*=2)
            {
                a=j&i;
                p=0;    q=6;
                b=-1;
                while(q!=0)
                {
//                    printf("%d %d\n",p,q);
                    if(b==-1)   q-=2;
                    if(mp[make_pair(p,q)] && b==-1)
                    {
                        q+=2;
                        if(a==0)    b=0;
                        else        b=1;
                        if(b==0)    p--,q--;
                        else        p++,q--;
                        if(mp[make_pair(p,q)])
                        {
                            if(b==0)    p++,q++;
                            else        p--,q++;
                            b^=1;   //
                            if(b==0)    p--,q--;
                            else        p++,q--;
                            if(mp[make_pair(p,q)])
                            {
                                if(b==0)    p++,q++;
                                else        p--,q++;
                                break;
                            }
                        }
                    }
                    else if(b!=-1)
                    {
                        if(b==0)    p--,q--;
                        else        p++,q--;
                        if(mp[make_pair(p,q)])
                        {
                            if(b==0)    p++,q++;
                            else        p--,q++;
                            break;
                        }
                    }
                }
                mp[make_pair(p,q)]=true;
            }
            if(mp[make_pair(x,y)])  co++;
        }
        printf("Case #%d: %lf\n",tt,co*2.0/(1<<N));
//        ss[make_pair(N,make_pair(x,y))]=co*2.0/(1<<N);
    }
}
