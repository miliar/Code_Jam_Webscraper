#include<iostream>
#include<stdio.h>
#include<cstring>
#include<vector>
#include<cstdlib>
using namespace std;
const int maxn=1000;
int n=32,need=500;
vector<int> prim;
int num=0;
int bitt[100],ans[100];
void calc_prime()
{
        for (int i=2;i<=1000;i++)
        {
                bool ok=true;
                for (int j=2;j<i;j++)
                        if (i%j==0) {
                                ok=false;
                                break;
                        }
                if (ok) prim.push_back(i);
        }
}
int check(__int128 x)
{
        for (int i=0;i<prim.size();i++)
        {
                if (prim[i]>=x) break;
                if (x%prim[i]==0)
                        return prim[i];
        }
        return 0;
}
void solve()
{

        for (int base=2;base<=10;base++)
        {
                __int128 now=0;
                for (int i=1;i<=n;i++)
                {
                        now=now*base+bitt[i];
                }
                ans[base]=check(now);
                if (ans[base]==0) return;
        }
        num++;
        for (int i=1;i<=n;i++)
                cout<<bitt[i];
        for (int i=2;i<=10;i++)
                cout<<" "<<ans[i];
        cout<<endl;
}
void dfs(int dep)
{
        if (num>=need) return;
        if (dep==n)
        {
                solve();
                return;
        }
        int tmp=rand()%2;
        bitt[dep]=tmp;
        dfs(dep+1);
        bitt[dep]=1-tmp;
        dfs(dep+1);
}
int main()
{
        int cas=0;
        printf("Case #%d: \n",++cas);
        calc_prime();
        bitt[1]=1;
        bitt[n]=1;
        dfs(2);
}
