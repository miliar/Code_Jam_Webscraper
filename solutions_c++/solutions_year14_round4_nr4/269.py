#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define MP make_pair

typedef double DB;
typedef long long LL;
typedef pair<int,int> PI;

const DB eps = 1e-6;
const int N = 1e2 + 7;
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;

struct Trie{
    int next[26];
} t[N];

int cnt, n, m, ans, res;

string s[100];
vector <int> v[100];

void Insert(int x, string s){
    for (int i = 0; i < s.size(); i++){
        if (!t[x].next[s[i] - 'A']) t[x].next[s[i] - 'A'] = ++cnt;
        x = t[x].next[s[i] - 'A'];
    }
}

int Calc(){
    int ret = 0;
    for (int i = 1; i <= m; i++){
        if (v[i].size() == 0) continue;
        memset(t, 0, sizeof(t));
        cnt = 1;
        for (int j = 0; j < v[i].size(); j++)
            Insert(1, s[v[i][j]]);
        ret += cnt;
    }
    return ret;
}
void Dfs(int x){
    if (x > n){
        int t = Calc();
        if (t > ans) ans = t, res = 1;
        else if (t == ans) res++;
        return;
    }
    for (int i = 1; i <= m; i++){
        v[i].PB(x);
        Dfs(x + 1);
        v[i].pop_back();
    }
}

int main(){
    int CAS;
    freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) cin >> s[i];
        ans = 0, res = 0;
        Dfs(1);
        printf("Case #%d: %d %d\n", cas, ans, res);
    }



}
