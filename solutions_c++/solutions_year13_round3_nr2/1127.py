/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
#define M 1000000007
struct state{
    int x;
    int y;
    int no;
    string moves;
};
map< pair< int,int > , int > MP;
string bfs(int dx,int dy)
{
    MP.clear();
    state a;
    a.x=0;a.y=0;a.no=1;a.moves="";
    queue<state>Q;
    Q.push(a);
    while(Q.empty()==false)
    {
        state a=Q.front();
        Q.pop();
        pair<int,int>pp=make_pair(a.x,a.y);
        if(MP[pp]!=0)continue;
        MP[pp]=1;
        if(a.x==dx && a.y==dy)return a.moves;
        if(a.no>=500)continue;
        state n;
        n.x=a.x+a.no;
        n.y=a.y;
        n.no=a.no+1;
        n.moves=a.moves+"E";
        Q.push(n);

        n.x=a.x-a.no;
        n.y=a.y;
        n.no=a.no+1;
        n.moves=a.moves+"W";
        Q.push(n);

        n.x=a.x;
        n.y=a.y+a.no;
        n.no=a.no+1;
        n.moves=a.moves+"N";
        Q.push(n);

        n.x=a.x;
        n.y=a.y-a.no;
        n.no=a.no+1;
        n.moves=a.moves+"S";
        Q.push(n);
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        int x,y;
        cin>>x>>y;
        printf("Case #%d: ",caseno++);
        cout<<bfs(x,y)<<endl;
    }
	return 0;
}
