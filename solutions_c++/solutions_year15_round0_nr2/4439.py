/* In the name of ALLAH, most gracious, most merciful */
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <ios>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <stack>

using namespace std;

typedef pair<int, int> pi;
typedef long long ll;

vector< int> v;
int ans;

void solve(int minute){
    if(minute == ans) return;
    vector< int > orig(v.begin(), v.end());
    sort(v.begin(), v.end(), greater<int>());
    if(v[0] == 1){
        ans = min(ans, minute);
        v = orig;
        return;
    }
    for(int i = 0; i < v.size(); i++){
        v[i]--;
    }
    solve(minute + 1);
    for(int i = 0; i < v.size(); i++){
        v[i]++;
    }
    v.push_back(0);
    for(int i = 1; i < v[0]; i++){
        v[v.size() - 1]++;
        v[0]--;
        solve(minute + 1);
    }
    v = orig;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    int T, n;
    cin >> T;
    for(int tt = 1; tt <= T; tt++){
        cin >> n;
        v.resize(n);
        for(int i = 0; i < n; i++){
            cin >> v[i];
        }
        ans = *max_element(v.begin(), v.end());
        solve(1);
        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
