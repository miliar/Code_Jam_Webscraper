#include <bits/stdc++.h>

using namespace std;

const int maxw = 10000;

map<string, int> st;
int bad_s[maxw], bad_f[maxw];
vector<int> g[maxw];
int used[maxw];
int con_with[maxw];
int cw[maxw];
int sz;

void init()
{
    st.clear();
    memset(bad_s, 0, sizeof(bad_s));
    memset(bad_f, 0, sizeof(bad_f));
    memset(used, 0, sizeof(used));
    memset(con_with, 0, sizeof(con_with));
    memset(cw, 0, sizeof(cw));
    for(int i = 0; i < maxw; i++)
        g[i].clear();
    sz = 1;
}

int dfs(int v)
{
    if(used[v])
        return 0;
    used[v] = 1;
    for(auto u: g[v])
    {
        if(!con_with[u] || dfs(con_with[u]))
        {
            con_with[u] = v;
            cw[v] = u;
            return 1;
        }
    }
    return 0;
}

int hs(string t)
{
    if(st[t]) return st[t];
    else return st[t] = sz++;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        init();
        cout << "Case #" << i << ": ";
        int n;
        cin >> n;
        vector<string> a[n];
        string s;
        getline(cin, s);
        for(int i = 0; i < n; i++)
        {
            getline(cin, s);
            stringstream ss;
            ss << s;
            while(ss >> s)
                a[i].push_back(s);
        }
        for(int j = 0; j < a[0].size(); j++)
            bad_s[hs(a[0][j])] = 1;
        for(int j = 0; j < a[1].size(); j++)
            bad_f[hs(a[1][j])] = 1;
        for(int i = 2; i < n; i++)
            for(int j = 0; j < a[i].size(); j++)
                for(int k = 0; k <= j; k++)
                {
                    if(!bad_s[hs(a[i][j])] && !bad_f[hs(a[i][k])])
                        g[hs(a[i][j])].push_back(hs(a[i][k]));
                    if(!bad_s[hs(a[i][k])] && !bad_f[hs(a[i][j])])
                        g[hs(a[i][k])].push_back(hs(a[i][j]));
                }
        int ans = 0;
        for(int i = 1; i < sz; i++)
            if(!bad_s[i] && dfs(i))
            {
                memset(used, 0, sizeof(used)), ans++;
            }
        for(int i = 1; i < sz; i++)
            ans += !cw[i] && !bad_s[i];
        for(int i = 1; i < sz; i++)
            ans += !con_with[i] && !bad_f[i];

        sz--;
        cout << sz - ans << "\n";
    }
}
