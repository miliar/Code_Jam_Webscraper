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
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define popc(i) (__builtin_popcountll(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 100005

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

vector<int>cap;
vector<int>item;
vector<int>tmp;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int n,x,var;
    int cas,loop=0;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d %d",&n,&x);
        item.clear();tmp.clear();cap.clear();

        for(int i=0;i<n;i++) {
            scanf("%d",&var);
            tmp.pb(var);
        }

        sort( tmp.rbegin() , tmp.rend() );

        int ans=0;
        while(SZ(tmp)!=0)
        {
            item.clear();cap.clear();
            int take=SZ(tmp)/2;
            if(SZ(tmp)%2) take++;


            for(int i=0;i<take;i++) cap.pb( x-tmp[i]);

            for(int i=take;i<SZ(tmp);i++) item.pb( tmp[i] );

//            for(int i=0;i<SZ(item);i++) deb("item",item[i]);
//            for(int i=SZ(cap)-1;i>=0;i--) deb("cap",cap[i]);


            int j=0;
            for(int i=SZ(cap)-1;i>=0;i--) // desc
            {
                for( ;j<SZ(item);j++) // desc
                {
                    if(cap[i]>=item[j])
                    {
//                        deb("packed ",item[j]);
                        item[j] = -1;
                        ++j;
                        break;
                    }
                }
            }

            tmp.clear();
            ans+=take;
            for(int i=0;i<SZ(item);i++) if(item[i]!=-1) tmp.pb( item[i] );
        }
        printf("Case #%d: %d\n",++loop,ans);
    }
    return 0;
}


