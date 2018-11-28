//#include<bits/stdc++.h>
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>
#include<unordered_set>
#include<unordered_map>



#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

#define deb(a)      cerr<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
#define popcount(a) (__builtin_popcountll(a))
#define SZ(a)       ((int)a.size())
#define fs           first
#define sc           second
#define pb          push_back
#define ll          long long
#define ld          long double
#define MP          make_pair
#define SS          stringstream
#define VS          vector<string>
#define VI          vector<int>
#define CON(a,b)  ((a).find(b)!=(a).end())
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))
#define accu(a,b,c) accumulate((a),(b),(c))
#define fi(i,a,b)   for(i=a;i<b;i++)
#define fii(a,b)    for(i=a;i<b;i++)
#define fij(a,b)    for(j=a;j<b;j++)
#define fik(a,b)    for(k=a;k<b;k++)
#define fil(a,b)    for(l=a;l<b;l++)
#define ri(i,a)     for(i=0;i<a;i++)
#define rii(a)      for(i=0;i<a;i++)
#define rij(a)      for(j=0;j<a;j++)
#define rik(a)      for(k=0;k<a;k++)
#define ril(a)      for(l=0;l<a;l++)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define ERR         (1e-7)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))




#define debug(a...)          {cout<<" #--> ";dbg,a; cout<<endl;}

struct debugger
{
    ///Collected from rudradevbasak
    template<typename T> debugger& operator , (const T v)
    {
        cout<<v<<" ";
        return *this;
    }
} dbg;


const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
typedef pair<int,int> pii;
typedef pair<char,pii> prp;

const int S = 102;
char bo[S][S];
char any[S][S][4];
pii anyPos[S][S][4];
int flg[S][S];

int r,c;
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
char dir[]="><v^";
int dtv[200];

///right ,left, down, up


bool valid(int cr,int cc)
{
    return -1<cr && cr<r && -1<cc && cc<c;
}

prp go(int pr,int pc,int dr,int dc)
{
    int i=1,cr,cc;
    while(true)
    {
        cr = pr+dr*i;
        cc = pc+dc*i;

        if(!valid(cr,cc))    return prp(0,pii(0,0));
        if(bo[cr][cc]!='.') return prp(bo[cr][cc],pii(cr,cc));
        i++;
    }
    return prp(0,pii(0,0));
}

bool isCycle;

void dfs(int i,int j)
{
    flg[i][j]=1;
    int v = dtv[bo[i][j]];
    v = any[i][j][v];
//    debug(i,j);
//    deb(v);
    if(v!=0)
    {
        v = dtv[c];
        pii t = anyPos[i][j][v];
        if(flg[t.fs][t.sc]!=0)
            isCycle=true;
        else dfs(t.fs,t.sc);
    }
    flg[i][j]=2;
}

int get()
{
    int i,j,k;
    prp cur;

    rii(r)
        rij(c)
            if(bo[i][j]!='.')
            {
                int cnt=0;

                rik(4)
                {
                    cur = go(i,j,dx[k],dy[k]);;
                    any[i][j][k]= cur.fs;
                    anyPos[i][j][k]=cur.sc;
                    cnt+=(any[i][j][k]>0);
                }
                if(!cnt)    return -1;
            }

    int ans=0;
    rii(r)
        rij(c)
            if(bo[i][j]!='.' && flg[i][j]==0)
            {
                isCycle=false;
                dfs(i,j);
//                deb(isCycle);
                ans+=!isCycle;
            }

    return ans;
}


int main()
{
//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


//    freopen("in.in","r",stdin);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.in","w",stdout);




    int i,j,k,tks=1,ks=1,n;

    cin>>tks;

    rii(4)
        dtv[ dir[i] ]=i;


    while(tks--)
    {
        scanf("%d%d",&r,&c);
        rii(r)
        {
            scanf("%s",bo[i]);
        }

        mem(flg,0);
        k=get();
        if(k==-1)   printf("Case #%d: IMPOSSIBLE\n",ks++);
        else printf("Case #%d: %d\n",ks++,k);
    }


    return 0;
}




