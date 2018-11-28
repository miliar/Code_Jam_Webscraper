#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n, m;
vector<int> rec;

void check(){
    vector<int> d;
    for (int base = 2; base < 11; ++ base){
        long long a = 0;
        bool h = false;
        for (int i = 0; i < n; ++ i)
            a = a * base + rec[i];
        for (long long i = 2; i <= sqrt(a); ++ i)
            if (a % i == 0){
                d.push_back(i);
                h = true;
                break;
            }
        if (h == false) return;
    }
    m --;
    for (int i = 0; i < n; ++ i)
        cout << rec[i];
    for (int i = 0; i < (int)d.size(); ++ i){
        cout << ' ' << d[i];
    }
    cout << endl;
}

void dfs(int c){
    if (m == 0) return;
    if (c + 1 == n){
        rec.push_back(1);
        check();
        rec.pop_back();
        return;
    }
    rec.push_back(1);
    dfs(c + 1);
    rec[c] = 0;
    dfs(c + 1);
    rec.pop_back();
}

int main(){
    freopen("C.out", "w", stdout);
    cin >> n >> m;
    printf("Case #1:\n");
    rec.push_back(1);
    dfs(1);
    fclose(stdout);

    return 0;
}
