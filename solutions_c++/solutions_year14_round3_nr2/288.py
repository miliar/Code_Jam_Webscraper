#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define MOD 1000000007

int N,i,j,T,s[300],e[300],sm[300], len[110], st[300], en[300], cnt;
char str[110][110];
bool vis[300], rec[300];
long long fact[200];
bool dfs(int v, int p);
vector<vector<int> > G;

int main()
{
    fact[0] = 1;
    for(i = 1; i < 200; i++)
        fact[i] = (fact[i-1] * i) % MOD;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d",&N);
        for(i = 0; i < N; i++)
        {
            scanf("%s",str[i]);
            //cout << str[i] << endl;
        }
        if(N == 1)
        {
            string x = str[0];
            int n = x.size();
            bool c = true;
            bool nv[300];
            memset(nv, 0, sizeof nv);
            for(i = 1; i < n; i++)
            {
                if(x[i] != x[i-1])
                    nv[x[i-1]] = true;
                if(nv[x[i]]){c = false; break;}
            } 
            printf("Case #%d: %d\n",t,(c?1:0));
            continue;
        }
        int z = 0;
        for(i = 0; i < N; i++)
        {
            int n = strlen(str[i]);
            len[i] = n;
            string m;
            for(j = 1; j < n-1; j++)
                if(str[i][j] != str[i][0] && str[i][j] != str[i][n-1])
                    m += str[i][j];
            for(j = 0; j < N; j++)
            {
                if(j == i) continue;
                for(auto it : m)
                {
                    string x;
                    x += it;
                    if(strstr(str[j],x.c_str()))
                    { z = 1; break; }
                }
                if(z == 1) break;
            }
            if(z == 1) break;
        }
        if(z == 1) 
        {
            printf("Case #%d: 0\n",t);
            continue;
        }
        memset(s, 0, sizeof s);
        memset(e, 0, sizeof e);
        memset(sm, 0, sizeof sm);
        memset(st, 0, sizeof st);
        memset(en, 0, sizeof en);
        G.clear();
        G.resize(60);
        cnt = 0;
        for(i = 0; i < N; i++)
        {
            if(str[i][0] == str[i][len[i]-1]) sm[str[i][0]]++;
            else
            {
                int x = str[i][0];
                int y = str[i][len[i]-1];
                if(st[x] == 0)                
                    st[x] = ++cnt;
                if(en[y] == 0)
                    en[y] = ++cnt;
                G[st[x]].pb(en[y]);
                G[en[y]].pb(st[x]);
                s[x]++;
                e[y]++;
            }
        }
        for(i = 'a'; i <= 'z'; i++)
            if(s[i] > 1 || e[i] > 1)
            { z = 1; break; }
        if(z == 1) 
        {
            printf("Case #%d: 0\n",t);
            continue;
        }
        for(i = 'a'; i <= 'z'; i++)
        if(st[i] && en[i])
        {
            G[st[i]].pb(en[i]);
            G[en[i]].pb(st[i]);
        }
        memset(vis, 0, sizeof vis);
        memset(rec, 0, sizeof rec);
        bool cyc = false;
        int cmps = 0;
        for(i = 1; i <= cnt; i++)
        {
            if(!vis[i])
            {
                cmps++;
                cyc = dfs(i, 0);         
                if(cyc) break;
            }
        }
        if(cyc)
        {
            printf("Case #%d: 0\n",t);
            continue;
        } 
        for(i = 'a'; i <= 'z'; i++)
            if(s[i] == 0 && e[i] == 0 && sm[i] != 0)
                cmps++;              
        long long ans = fact[cmps];
        for(i = 'a'; i <= 'z'; i++)
            ans = (ans * fact[sm[i]]) % MOD;
        printf("Case #%d: %lld\n",t,ans);
    }
    
    return 0;
}

bool dfs(int v, int p)
{
    vis[v] = true;
    rec[v] = true;
    //cout << v << " in\n";
    for(auto x : G[v])    
    {
        if(x == p) continue;
        //cout << x << " " << vis[x] << " " << rec[x] << endl;
        if(!vis[x] && dfs(x, v))
            return true;
        else if(rec[x])
            return true;
    }
    rec[v] = false;
    //cout << v << " out\n";
    return false;
}
