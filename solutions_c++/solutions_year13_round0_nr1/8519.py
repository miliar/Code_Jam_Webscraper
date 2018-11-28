#include<iostream>
#include<string>
#include<cstring>
#include<map>
#include<queue>
#include<deque>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<sstream>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)<(b)?(b):(a))
#define PI 2*acos(0.0)
#define ERR 1e-9
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )
#define dist4adj(x1,y1,x2,y2) ( abs(x1-x2) + abs(y1-y2) )
#define dist8adj(x1,y1,x2,y2) max( abs(x1-x2) , abs(y1-y2) )
#define Wait system("pause")
#define Time printf("time=%.3lf sec.\n",(double) (clock())/CLOCKS_PER_SEC)

#define pii pair<int,int>
#define mii map<int,int>
#define F first
#define S second
#define Mp make_pair

#define pcnt(i) __builtin_popcount(i)
#define pb push_back
#define Sz size()
#define all(x) (x).begin(),(x).end()
#define Set(b,a) memset(b,a,sizeof b)
#define print2(x) printf("Case %d: %d\n",cse++,x)
#define print1 printf("Case %d:\n",cse++)
#define printn(a) printf("%ld\n",a)
#define tin(x) scanf("%d",&x)
#define tin2(x,y) scanf("%d%d",&x,&y)
#define tin3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define Rep(i,n) for(int i=0;i<n;i++)
#define Mod 10000000007
#define INF 1<<30
#define SINF 0x0f0f0f0f
#define Max 500010

ll Pow(ll B,ll P){  ll R=1; while(P>0)  {if(P%2==1) R=(R*B);P/=2;B=(B*B);}return R;}
int BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;}

template<class T1> void deb(T1 e){cerr<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cerr<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cerr<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cerr<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}

//int dx[]={1,0,-1,0}; int dy[]={0,1,0,-1}; ///4 ways
//int dx[]={1,1,0,-1,-1,-1,0,1}; int dy[]={0,1,1,1,0,-1,-1,-1}; ///8 ways
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1}; ///knight moves

int main()
{

    //freopen("inn.in","r",stdin);
    //freopen("ouut.txt","w",stdout);
    int t;
    tin(t);
    int h=1;

    while(t--)
    {
        map<char,int> mp;
        string s[5];
        for(int i=0;i<4;i++)
        {
            cin>>s[i];
        }
        bool found=0;
        for(int i=0;i<4;i++)
        {
            char pre='\0';
            for(int j=0;j<4;j++)
            {
                if(j==0) pre=s[i][j];
                if(pre=='T') break;
                if(s[i][j]=='.')break;
                else if(s[i][j]!=pre&&j!=3) break;
                else if((s[i][j]=='T'&&j==3)||(s[i][j]==pre&&j==3)){ mp[pre]=1; found=1;}
            }
        }
        if(!found)
        {
            for(int i=0;i<4;i++)
            {
                char pre='\0';
                for(int j=3;j>=0;j--)
                {
                    if(j==3) pre=s[i][j];
                    if(pre=='T') break;
                    if(s[i][j]=='.')break;
                    else if(s[i][j]!=pre&&j!=0) break;
                    else if((s[i][j]=='T'&&j==0)||(s[i][j]==pre&&j==0)){ mp[pre]=1; found=1;}
                }
            }
        }
        if(!found)
        {
            for(int i=0;i<4;i++)
            {
                char pre='\0';
                for(int j=3;j>=0;j--)
                {
                    if(j==3) pre=s[j][i];
                    if(pre=='T') break;
                    if(s[j][i]=='.')break;
                    else if(s[j][i]!=pre&&j!=0) break;
                    else if((s[j][i]=='T'&&j==0)||(s[j][i]==pre&&j==0)){ mp[pre]=1; found=1;}
                }
            }
        }
        if(!found)
        {
            for(int i=0;i<4;i++)
            {
                char pre='\0';
                for(int j=0;j<4;j++)
                {
                    if(j==0) pre=s[j][i];
                    if(pre=='T') break;
                    if(s[j][i]=='.')break;
                    else if(s[j][i]!=pre&&j!=3) break;
                    else if((s[j][i]=='T'&&j==3)||(s[j][i]==pre&&j==3)){ mp[pre]=1; found=1;}
                }
            }
        }
        if(!found)
        {
            if(s[0][0]=='X'||s[0][0]=='O')
            {
                if(s[0][0]==s[1][1]&&s[1][1]==s[2][2])
                {
                    if(s[3][3]=='T'||s[0][0]==s[3][3]) {mp[s[0][0]]=1;found=1;}
                }
            }
            if(s[3][3]=='X'||s[3][3]=='O')
            {
                if(s[3][3]==s[1][1]&&s[1][1]==s[2][2])
                {
                    if(s[0][0]=='T'||s[0][0]==s[3][3]) {mp[s[2][2]]=1;found=1;}
                }
            }
            if(s[0][3]=='X'||s[0][3]=='O')
            {
                if(s[1][2]==s[0][3]&&s[2][1]==s[1][2])
                {
                    if(s[3][0]=='T'||s[0][3]==s[3][0]) {mp[s[1][2]]=1;found=1;}
                }
            }
            if(s[3][0]=='X'||s[3][0]=='O')
            {
                if(s[1][2]==s[3][0]&&s[2][1]==s[1][2])
                {
                    if(s[0][3]=='T'||s[0][3]==s[3][0]) {mp[s[1][2]]=1;found=1;}
                }
            }
        }




        if(found)
        {
            if(mp['X']) printf("Case #%d: X won\n",h++);
            else printf("Case #%d: O won\n",h++);
        }
        else
        {
            bool noo=0;
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    if(s[i][j]=='.') noo=1;
                }
            }

            if(noo) printf("Case #%d: Game has not completed\n",h++);
            else printf("Case #%d: Draw\n",h++);
        }
    }
}
