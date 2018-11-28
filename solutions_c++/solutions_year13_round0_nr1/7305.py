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
int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

vector<string>v;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int X,O,complete;
    string str;
    char arr[100];
    int cas,loop=0;
    scanf("%d",&cas);
    while(cas--)
    {
        v.clear();
        for(int i=0;i<4;i++) scanf("%s",arr), str=arr,v.pb(str);

        X=O=0;

        int xx,oo,tt;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                for(int p=0;p<8;p++)
                {
                    xx=oo=tt=0;
                    int now_x=i,now_y=j,cnt=1;

                    if(v[now_x][now_y]=='X') xx++;
                    else if(v[now_x][now_y]=='O') oo++;
                    else if(v[now_x][now_y]=='T') tt++;

                    while(cnt<4)
                    {
                        now_x=now_x+rrr[p];
                        now_y=now_y+ccc[p];
                        if(now_x<0 || now_y<0 || now_x>=4 || now_y>=4) break;

                        if(v[now_x][now_y]=='X') xx++;
                        else if(v[now_x][now_y]=='O') oo++;
                        else if(v[now_x][now_y]=='T') tt++;
                        cnt++;
                    }
                    if(xx+tt==4) X++;
                    else if(oo+tt==4) O++;
                }
            }

        complete=1;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(v[i][j]=='.') complete=0;
        printf("Case #%d: ",++loop);

        if(X) puts("X won");
        else if(O) puts("O won");
        else if(complete) puts("Draw");
        else puts("Game has not completed");

    }

    return 0;
}

