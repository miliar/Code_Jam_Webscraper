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

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

struct data{

    int day;
    int left,right;
    int strength;
    data(int a, int b, int c, int d)
    {
        day=a;left=b;right=c;strength=d;
    }
};

vector<data>query;
vector<data>update;

bool com(data a, data b)
{
    return a.day<b.day;
}

map<int,int>wall;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ans;
    int d,w,e,s,ni,delta_d,delta_p,delta_s;
    int cas,loop=0,n;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&n);
        query.clear();update.clear();
        for(int i=0;i<n;i++)
        {
            scanf("%d %d %d %d %d %d %d %d",&d,&ni,&w,&e,&s,&delta_d,&delta_p,&delta_s);

            for(int day=d , cnt=0 ,left=w,right=e, strength=s ; cnt<ni ; cnt++, day+=delta_d, left+=delta_p , right+=delta_p , strength+=delta_s )
            {
                query.pb( data(day,left,right,strength) );

            }
        }
        ans=0;
        wall.clear();for(int i=-1000;i<=1000;i++) wall[i]=0;
        sort(all(query),com);

        int next_day;
//        int now_l,now_r;
//        int now_ss;

        for(int i=0;i<SZ(query);i++)
        {
            int dd=query[i].day;
            int l=query[i].left;
            int r=query[i].right;
            int ss=query[i].strength;

            l*=2;
            r*=2;

//            deb(dd,l,r,ss);

            int flag=0;
            for(int p=l;p<=r;p++)
            {
                if(wall[p]<ss) {flag=1;break;}
            }
//            deb("victory",flag);
            ans+=flag;

            if(i<SZ(query)) next_day= query[i+1].day;
            else next_day=oo;

            if(next_day==dd)
            {
                update.pb( data(dd,l,r,ss) );
                //for(int p=l;p<=r;p++) wall[p] =max ( wall[p] ,now_ss);
            }else
            {
                update.pb( data(dd,l,r,ss) );
                for(int uu=0;uu<SZ(update);uu++)
                {
                    for(int p=update[uu].left;p<=update[uu].right;p++) wall[p] =max ( wall[p] ,update[uu].strength);
                }
                update.clear();
            }
        }
        printf("Case #%d: %d\n",++loop,ans);
    }

    return 0;
}

