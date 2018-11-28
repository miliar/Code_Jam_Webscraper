#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#define y second
#define x first
#define intpair pair<int,int>
#define mp make_pair
using namespace std;
const int jump[4][4][2]={
    0,0,0,1,0,2,0,3,
    0,1,1,0,0,3,1,2,
    0,2,1,3,1,0,0,1,
    0,3,0,2,1,1,1,0
};
int t,l,x,cas=0;
string s;
inline intpair operator *(intpair x,intpair y)
{
    return make_pair(x.x^y.x^jump[x.y][y.y][0],jump[x.y][y.y][1]);
}
void power(intpair &ans,intpair base,int n)
{
    if(n==1)
    {
        ans=base;
        return;
    }
    power(ans,base,n>>1);
    ans=ans*ans;
    if(n&1) ans=ans*base;
}
bool check2(int p,int q)
{
    if(q>=l) p++,q=0;
    intpair cur=mp(0,0);
    for(int j=q;j<l;j++)
    {
        cur=cur*mp(0,s[j]-'h');
        if(cur.x==0 && cur.y==2) return true;
    }
    for(int i=p+1;i<=x;i++)
        for(int j=0;j<l;j++)
    {
        cur=cur*mp(0,s[j]-'h');
        if(cur.x==0 && cur.y==2) return true;
    }
    return false;
}
bool check1()
{
    intpair cur=mp(0,0);
    bool vis[2][4];
    for(int i=1;i<=x;i++)
        for(int j=0;j<l;j++)
    {
        cur=cur*mp(0,s[j]-'h');

        if(cur.x==0 && cur.y==1 )
            return check2(i,j+1);
    }
    return false;
}
int main()
{
    freopen("C-small-attempt9.in","r",stdin);
    freopen("Dijkstra.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>l>>x>>s;
        pair<int,int>ans=mp(0,0);
        for(int i=0;i<l;i++)
        {
            int cur=s[i]-'h';
            ans=mp(ans.x^jump[ans.y][cur][0],jump[ans.y][cur][1]);
        }
        power(ans,ans,x);
        cout<<"Case #"<<++cas<<": ";
        if(ans.x==1 && ans.y==0 && check1()) puts("YES");
        else puts("NO");
    }
}
