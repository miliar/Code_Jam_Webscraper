#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1 << 30;
const double EPS = 1e-8;

int onboard(int x, int y, int r, int c)
{
    if(x<0 || x>=r) return 0;
    if(y<0 || y>=c) return 0;
    return 1;
}

int kk(int x, int y, vector<string>& v, int r, int c)
{
    int m[4][2]={{0,1},{-1,0},{0,-1},{1,0}};
    int d=0;
    if(v[x][y]=='v') d=3;
    if(v[x][y]=='<') d=2;
    if(v[x][y]=='^') d=1;
    while(onboard(x,y,r,c))
    {
        x+=m[d][0];
        y+=m[d][1];
        if(!onboard(x,y,r,c)) return 0;
        if(v[x][y]!='.') return 1;
    }
    return 0; //shouldnt happen?
}

void solve(int num)
{
    int r,c;
    cin>>r>>c;
    vector<string> v(r);
    for(int i=0;i<r;i++) cin>>v[i];
    int ans=0, fail=0;
    char pos[4]={'^','>','v','<'};

    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            if(v[i][j]=='.') continue;
            if(!kk(i,j,v,r,c))
            {
                int oks=0;
                for(int k=0;k<4;k++)
                {
                    v[i][j]=pos[k];
                    if(kk(i,j,v,r,c)) oks=1;
                }
                if(oks) ans++;
                else fail=1;
            }
        }
    }

    cout<<"Case #"<<num<<": ";
    if(fail) cout<<"IMPOSSIBLE\n";
    else cout<<ans<<"\n";

}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

