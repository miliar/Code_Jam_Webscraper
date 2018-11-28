#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>

using namespace std;

#define SZ(x) ((int)x.size())
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define clrall(name,val) memset(name,(val),sizeof(name));
#define EPS 10e-9
#define ll long long
#define ull long long unsigned
#define sf scanf
#define pf printf
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo (1<<28)
#define mp make_pair
#define mt make_tuple
#define get(a,b) get<b>(a)
#define fs first
#define sc second
#define Read freopen("S.in","r",stdin)
#define Write freopen("S.out","w",stdout)
#define __ std::ios_base::sync_with_stdio (false)

ll MulModL(ll B,ll P,ll M) {    ll R=0; while(P>0)      { if((P&1ll)==1) { R=(R+B); if(R>=M) R-=M; } P>>=1ll; B=(B+B); if(B>=M) B-=M; } return R; }

ll MulModD(ll B, ll P,ll M) {   ll I=((long double)B*(long double)P/(long double)M);    ll R=B*P-M*I; R=(R%M+M)%M;  return R; }

ll BigMod(ll B,ll P,ll M) {     ll R=1; while(P>0)      { if(P%2==1) { R=(R*B)%M; } P/=2; B=(B*B)%M; } return R; } /// (B^P)%M

template<class T1> void deb(T1 e1){cout<<e1<<"\n";}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<"\n";}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<"\n";}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<"\n";}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6,class T7> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6,T7 e7){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<" "<<e7<<"\n";}

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

struct data
{
    int v;
    char c;

    data(){}
    data(int v,char c):v(v),c(c){}
    bool operator < (const data &x)const
    {
        return v<x.v;
    }
};

void copyQ(priority_queue<data> q,priority_queue<data> &tq)
{
    while(!tq.empty()) tq.pop();
    while(!q.empty()) tq.push(q.top()),q.pop();
    return ;
}

bool isOK(priority_queue<data> q,int ttot)
{
    data tv;
    while(!q.empty())
    {
        tv=q.top();
        q.pop();
        if(tv.v*2>ttot)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    Read;
    Write;
    int t,n,cas=0;
    int p[30];
    int tot=0;
    priority_queue<data> q,tq,mq;
    vector<data> val;
    string res;
    sf("%d",&t);
    while(t--)
    {
        sf("%d",&n);
        while(!q.empty()) q.pop();
        val.clear();
        res="";
        tot=0;
        for(int i=0;i<n;i++)
        {
            sf("%d",&p[i]);
            q.push(data(p[i],(i+'A')));
            tot+=p[i];
        }
        bool sp=false;
        while(!q.empty())
        {
            val.clear();
            copyQ(q,tq);
            data v=q.top();
            data tv=v;
            int ttot=tot;
            tv.v--;
            ttot--;
            q.pop();
            if(tv.v)
            {
                q.push(tv);
            }
            copyQ(q,mq);
            if(isOK(q,ttot))
            {
                copyQ(mq,q);
                tot--;
                if(sp)
                    res+=" ";
                sp=true;
                res+=v.c;
                continue;
            }
            copyQ(tq,q);
            v=q.top();
            tv=v;
            if(tv.v>=2)
            {
                tv.v-=2;
                ttot=tot-2;
                if(tv.v)
                {
                    q.push(tv);
                }
                copyQ(q,mq);
                if(isOK(q,ttot))
                {
                    copyQ(mq,q);
                    tot-=2;
                    if(sp)
                        res+=" ";
                    sp=true;
                    res+=v.c;
                    res+=v.c;
                    continue;
                }
            }
            copyQ(tq,q);
            if(SZ(q)>=2)
            {
                data v1,v2;
                v1=q.top();
                q.pop();
                v2=q.top();
                q.pop();
                data tv1,tv2;
                tv1=v1;
                tv2=v2;
                tv1.v--;
                tv2.v--;
                ttot=tot-2;
                if(tv1.v)
                {
                    q.push(tv1);
                }
                if(tv2.v)
                {
                    q.push(tv2);
                }
                copyQ(q,mq);
                if(isOK(q,ttot))
                {
                    copyQ(mq,q);
                    tot-=2;
                    if(sp)
                        res+=" ";
                    sp=true;
                    res+=v1.c;
                    res+=v2.c;
                    continue;
                }
            }
        }
        pf("Case #%d: %s\n",++cas,res.c_str());
    }

    return 0;
}










