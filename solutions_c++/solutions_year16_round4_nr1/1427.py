#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cassert>
#include <sstream>


using namespace std;

typedef long long LL;

void half_sort(string& str, int b, int e){
    if(e <= b+1) return;
    int m = (e+b) / 2;
    int w = (e-b) / 2;
    half_sort(str, b, m);
    half_sort(str, m, e);
    bool flag = false;
    for(int i = b; i < m; ++i){
        if(str[i] < str[i+w]) break;
        if(str[i] > str[i+w]){
            flag = true;
            break;
        }
    }
    if(flag){
        for(int i = b; i < m; ++i){
            swap(str[i], str[i+w]);
        }
    }
}

void gen(LL n, string prev, LL& r, LL& p, LL& s, string& next){
    for(int i = 0; i < n; ++i){
        next = string(1<<(i+1), '?');
        for(int j = 0; j < prev.size(); ++j){
            if(prev[j] == 'R'){
                next[j*2+0] = 'R';
                next[j*2+1] = 'S';
                s += 1;
            }else if(prev[j] == 'P'){
                next[j*2+0] = 'P';
                next[j*2+1] = 'R';
                r += 1;
            }else if(prev[j] == 'S'){
                next[j*2+0] = 'P';
                next[j*2+1] = 'S';
                p += 1;
            }
        }
        half_sort(next, 0, next.size());
        prev = next;
    }
}

string solve(LL n, LL r, LL p, LL s){
    LL r2, p2, s2;
    string str;
    r2 = 1; p2 = 0; s2 = 0;
    gen(n, "R", r2, p2, s2, str);
    if(r2 == r && p2 == p && s2 == s){
        return str;
    }
    r2 = 0; p2 = 1; s2 = 0;
    gen(n, "P", r2, p2, s2, str);
    if(r2 == r && p2 == p && s2 == s){
        return str;
    }
    r2 = 0; p2 = 0; s2 = 1;
    gen(n, "S", r2, p2, s2, str);
    if(r2 == r && p2 == p && s2 == s){
        return str;
    }
    return "IMPOSSIBLE";
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        cout << "Case #" << t << ": " << solve(n, r, p, s) << endl;
    }
    return 0;
}

