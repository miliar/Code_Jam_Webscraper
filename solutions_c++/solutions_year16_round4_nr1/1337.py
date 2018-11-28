#include <bits/stdc++.h>
using namespace std;

int p, r, s;

string dfs(int d, int x, int f){
    if(d == f){
        if(x == 0){
            p++;
            return string("P");
        } else if(x == 1){
            r++;
            return string("R");
        } else {
            s++;
            return string("S");
        }
    } else {
        string a, b;
        a = dfs(d+1, x, f);
        b = dfs(d+1, (x+1)%3, f);
        return a < b ? a + b : b + a;
    }
}
void Solve(int tests){
    int d, x, y, z;
    scanf("%d%d%d%d", &d, &y, &x, &z);
    vector<string> ans;
    for(int i = 0 ; i < 3 ; i++){
        p = r = s = 0;
        string str = dfs(0, i, d);
        if(p == x && r == y && s == z){
            ans.push_back(str);
        }
    }
    sort(ans.begin(), ans.end());
    if(ans.size()){
        printf("Case #%d: %s\n", tests, ans[0].c_str());
    } else {
        printf("Case #%d: IMPOSSIBLE\n", tests);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1 ; i <= n ; i++){
        Solve(i);
    }

    return 0;
}
