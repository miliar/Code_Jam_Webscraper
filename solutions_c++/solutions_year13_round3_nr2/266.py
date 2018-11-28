#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> paii;
typedef pair< ll, ll > pall;


#define PI (2.0*acos(0))
#define ERR 1e-5
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Contains(X,item)        ((X).find(item) != (X).end())
#define popc(i) (__builtin_popcountll(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 100050
#define twoL(X) (((ll)(1))<<(X))

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}


template<class T> T Abs(T x) {return x > 0 ? x : -x;}
template<class T> inline T sqr(T x){return x*x;}
ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
ll BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

map< paii , int >M;
map<paii, paii>par;

struct data
{
    paii pt;
    int jmp;
    data( paii xx , int yy)
    {
        pt=xx;jmp=yy;
    }
};


void bfs()
{
    M[mp(0,0)]=0;
    queue<data>Q;
    Q.push( data( mp(0,0) ,0 ) );

    paii now,to;
    int jmp;
    while(!Q.empty())
    {
        now=Q.front().pt;
        jmp=Q.front().jmp;
        Q.pop();

//        deb(now.fs,now.sc,"jump",jmp);
//        deb("par ",par[now].fs, par[now].sc);

        jmp++;
        for(int i=0;i<4;i++)
        {
            to.fs=now.fs + rrr[i]*jmp;
            to.sc=now.sc + ccc[i]*jmp;

            if( abs( to.fs )>100 || abs(to.sc)>100 ) continue;

            if(M.find( to) ==M.end())
            {
                Q.push( data(to,jmp) );
                M[to]=jmp;
                par[ to ]=now;
            }
        }
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    par.clear();
    M.clear();

    paii cord;
    string sol;
    int x,y,x2,y2;
    bfs();
    int cas,loop=0;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d %d",&x,&y);
        printf("Case #%d: ",++loop);

        sol.clear();
        while(x!=0 || y!=0 )
        {
            cord=par[ mp(x,y) ];

//            deb("now ",x,y);
            x2=cord.fs;
            y2=cord.sc;

//            deb("par ",x2,y2);

            if(y2==y)
            {
                if(x2<x) sol.pb('E');
                else sol.pb('W');
            }else {
                if(y2<y) sol.pb('N');
                else sol.pb('S');
            }
            x=x2;
            y=y2;
        }
        reverse(all(sol));
        cout<<sol<<endl;
    }

    return 0;
}

