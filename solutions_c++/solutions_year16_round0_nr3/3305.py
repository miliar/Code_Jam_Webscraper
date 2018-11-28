#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int sv[1000006];
vector<ll> pr;
vector<int> ans;

void fill_sv(int n)
{
    int i,j;
    for(i=2;i<=n;i++)
    {
        if(!sv[i])
        {
            pr.push_back(i);
            for(j=2*i;j<=n;j+=i)
            {
                sv[j] = 1;
            }
        }
    }
}

string gen(int n)
{
    string ret = "1";
    for(int i=1;i<n-1;i++)
    {
        if(rand()&1)
            ret += '1';
        else
            ret += '0';
    }
    ret += '1';
    return ret;
}

ll powmod(ll b,ll e,ll m)
{
    ll ret = 1;
    while(e)
    {
        if(e&1)
        {
            ret *= b;
            ret %= m;
        }
        b *= b;
        b %= m;
        e >>= 1;
    }
    return ret;
}


bool check(string &x)
{
    int n = x.length();
    for(int i=2;i<=10;i++)
    {
        bool f=false;
        for(int j=0;j<int(pr.size());j++)
        {
            ll sum = 0;
            for(int k=n-1;k>=0;k--)
            {
                if(x[k] == '1')
                {
                    sum += powmod(i,n-k-1,pr[j]);
                    sum %= pr[j];
                }
            }
            if(sum == 0)
            {
                ans.push_back(pr[j]);
                f=true;
                break;
            }
        }
        if(!f)
         return false;
    }
    return true;
}

map<string,bool> mp;

int main()
{
    fill_sv(10000);
    time_t T;
    time(&T);
    srand(T);
    int cnt = 0;
    freopen("out.txt","w",stdout);
    cout<<"Case #1: "<<endl;
    while(cnt<500)
    {
        string X = gen(32);
        ans.clear();
        if(check(X))
        {
            if(mp.count(X))
                continue;
            mp[X] = true;
            cnt++;
            //cout<<cnt++<<endl;
            cout<<X<<" ";
            for(int i=0;i<ans.size();i++)
                cout<<ans[i]<<" ";
            cout<<endl;
            //system("pause");
        }
    }
    //system("pause");
    return 0;
}
