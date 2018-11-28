#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mod 1000000007
#define reset(s,val) memset(s,val,sizeof(s))
#define eps 1e-12
#define pi acos(-1)
#define sqr(x) (x)*(x)
#define two(x) (1<<(x))

int t,r,c,ans;
string grid[111];
bool flag;

bool haveup(int x,int y)
{
    For(i,0,x) if(grid[i][y]!='.') return true;
    return false;
}
bool haveleft(int x,int y)
{
    For(i,0,y) if(grid[x][i]!='.') return true;
    return false;
}
bool haveright(int x,int y)
{
    For(i,y+1,c) if(grid[x][i]!='.') return true;
    return false;
}
bool havedown(int x,int y)
{
    For(i,x+1,r) if(grid[i][y]!='.') return true;
    return false;
}

int main( ){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //ios::sync_with_stdio(0);
    cin>>t;
    For(cas,1,t+1)
    {
        cout<<"Case #"<<cas<<": ";
        ans=0;
        cin>>r>>c;
        For(i,0,r) cin>>grid[i];
        flag=false;
        For(i,0,c)
        {
            For(j,0,r) if(grid[j][i]!='.')
            {
                if(grid[j][i]=='^') ans++;
                if(!(havedown(j,i)||haveleft(j,i)||haveright(j,i))) flag=true;
                break;
            }
            for(int j=r-1;j>=0;j--) if(grid[j][i]!='.')
            {
                if(grid[j][i]=='v') ans++;
                if(!(haveup(j,i)||haveleft(j,i)||haveright(j,i))) flag=true;
                break;
            }
        }
        For(i,0,r)
        {
            For(j,0,c) if(grid[i][j]!='.')
            {
                if(grid[i][j]=='<') ans++;
                if(!(haveup(i,j)||haveright(i,j)||havedown(i,j))) flag=true;
                break;
            }
            for(int j=c-1;j>=0;j--) if(grid[i][j]!='.')
            {
                if(grid[i][j]=='>') ans++;
                if(!(haveup(i,j)||havedown(i,j)||haveleft(i,j))) flag=true;
                break;
            }
        }
        if(flag) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
}
