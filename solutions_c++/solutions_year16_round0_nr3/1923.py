#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i = 0; i < (int)(n); ++i)

int calcMod(const string &s, int base, int mod){
    int sum = 0;
    rep(i,s.size()){
        sum *= base;
        sum %= mod;
        sum += s[i]-'0';
        sum %= mod;
    }
    return sum;
}

int diviser(const string& s, int base){
    int ps[] = {2,3,5,7,11,13};
    for(auto &p : ps){
        if(calcMod(s,base,p) == 0) return p;
    }
    return -1;
}

int N,J;

int done;
void rec(int k, int rem, string &cur){
    if(done >= J) return;
    if(k+1 == N){
        if(rem == 1){
            cur += '1';
            int a = diviser(cur,2);
            int b = diviser(cur,6);
            int c = diviser(cur,8);
            if(a != -1 && b != -1 && c != -1){
                if(done < J){
                    assert(calcMod(cur,2,a) == 0);
                    assert(calcMod(cur,3,2) == 0);
                    assert(calcMod(cur,4,3) == 0);
                    assert(calcMod(cur,5,2) == 0);
                    assert(calcMod(cur,6,b) == 0);
                    assert(calcMod(cur,7,2) == 0);
                    assert(calcMod(cur,8,c) == 0);
                    assert(calcMod(cur,9,2) == 0);
                    assert(calcMod(cur,10,3) == 0);
                    printf("%s %d %d %d %d %d %d %d %d %d\n",
                           //           2  3  4  5  6  7  8  9 10
                           cur.c_str(), a, 2, 3, 2, b, 3, c, 2, 3);
                    ++done;
                }
            }
            cur.pop_back();
        }
    } else {
        cur += '0';
        rec(k+1,rem,cur);
        cur.pop_back();
        if(rem != 1){
            cur += '1';
            rec(k+1,rem-1, cur);
            cur.pop_back();
        }
    }
}

void solve(){
    // assert(N == 32);
    string tmp = "1";
    done = 0;
    rec(1,5,tmp);
    assert(done == J);
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; ++i){
        cin >> N >> J;
        // assert(n == 32 && j == 500);
        printf("Case #%d:\n", i+1);
        solve();
    }
}
