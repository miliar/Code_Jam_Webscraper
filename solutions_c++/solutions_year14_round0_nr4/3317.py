#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;

double a[100500], b[100500];
vector <int> g[100500];
int n;
int u[100500], uc = 0;
int p[100500];

bool dfs (int x){
    if (u[x] == uc)  return 0;
    u[x] = uc;
    for (int i = 0; i < g[x].size(); i++) {
        int j = g[x][i];
        if (p[j] == -1 || dfs (p[j])) {
            p[j] = x;
            return 1;
        }
    }
    return 0;
}

int calc () {
    int res= 0 ;
    for (int i = 0; i < n; i++) p[i] = -1;
    for (int i = 0; i < n; i++) {
        uc++;
        if (dfs(i)) res++;
    }
    return res;
}

void solve () {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i], g[i].clear();
    for (int i = 0; i < n; i++) cin >> b[i];
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (a[i] > b[j]) g[i].push_back(j);
    
    cout << calc() << " ";
    for (int i = 0; i < n; i++) g[i].clear();
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (a[i] < b[j]) g[i].push_back(j);
    cout << n-calc() << endl;
    
}

int main (){
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
