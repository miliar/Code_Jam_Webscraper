#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
// Let's Fight!

const int MAXN = 111;

int R, C;
int pre[MAXN][MAXN];
int ans[MAXN][MAXN];

vector< vector<int> > genvv(int c)
{
    vector< vector<int> > ret;
    vector< vector<int> > tmp;
    ret.PB(vector<int>());
    for(int i=0; i<c; i++)
    {
        for(auto v: ret)
        {
            for(int j=1; j<=3; j++)
            {
                tmp.PB(v);
                tmp.back().PB(j);
            }
        }
        ret = tmp;
        tmp.clear();
    }

    return ret;
}

void calc()
{
    for(int c=1; c<=6; c++)
    {
        map< vector<int>, int > mp;
        vector< vector<int> > vv = genvv(c);
        for(auto v: vv)
        {
            vector<int> cnt;
            bool ok = true;
            for(int i=0; i<c; i++)
            {
                int r = 0;
                if(v[(i+c-1)%c]==v[i]) r++;
                if(v[(i+1)%c]==v[i]) r++;
                if(v[i] == r) cnt.PB(v[i]*2+1);
                else if(v[i] == r+1) cnt.PB(v[i]*2);
                else
                {
                    ok = false;
                    break;
                }
            }
            if(!ok) continue;
            // for(auto i: cnt) cout<<i<<" ";cout<<endl;
            mp[cnt] = 1;
        }

        // cout<<c<<" : "<<mp.size()<<endl;

        for(int i=2; i<=6; i++)
        {
            map< vector<int>, int> nmp;
            for(auto pr: mp)
            {
                vector<int> v = pr.F;
                int vcnt = pr.S;
                for(auto u: vv)
                {
                    bool ok = true;
                    vector<int> cnt;
                    for(int j=0; j<c; j++)
                    {
                        int aa = v[j]/2, bb = v[j]%2;
                        if((aa==u[j] && bb==1) || (aa!=u[j] && bb==0))
                        {
                            ok = false;
                            break;
                        }
                        int r = 0;
                        if(u[(j+1)%c] == u[j]) r++;
                        if(u[(j+c-1)%c] == u[j]) r++;
                        if(u[j] == aa) r++;
                        if(u[j] == r) cnt.PB(2*u[j]+1);
                        else if(u[j] == r+1) cnt.PB(2*u[j]);
                        else
                        {
                            ok = false;
                            break;
                        }
                    }
                    if(!ok) continue;
                    nmp[cnt] += vcnt;
                }
            }
            mp = nmp;
            for(auto pr: mp)
            {
                vector<int> v = pr.F;
                int vcnt = pr.S;
                bool ok = true;
                for(int j=0; j<c; j++)
                {
                    if(v[j]%2==0)
                    {
                        ok = false;
                        break;
                    }
                }
                if(!ok) continue;
                pre[i][c] += vcnt;
            }
            // cout<<i<<","<<c<<" = "<<pre[i][c]<<endl;

            for(int j=1; j<=c; j++)
            {
                int rot = __gcd(j, c);
                ans[i][c] += pre[i][rot];
            }
            ans[i][c] /= c;
        }
    }
}

int main()
{
    calc();
    IOS;
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        cin>>R>>C;
        cout<<"Case #"<<tt<<": "<<ans[R][C]<<endl;
    }
    return 0;
}
