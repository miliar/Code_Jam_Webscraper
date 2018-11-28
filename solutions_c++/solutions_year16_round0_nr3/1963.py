#include <iostream>
#include <string>
#include <vector>
#include <string>

using namespace std;

typedef long long LL;

bool divisible(LL v, LL base, LL p){
    LL res = 0;
    LL r = 1;
    while(v > 0){
        if(v & 1){
            res += r;
            res %= p;
        }
        v >>= 1;
        r = r*base % p;
    }
    return res % p == 0;
}

void check(LL n, LL v, vector<LL>& div){
    for(LL base = 2; base <= 10; ++base){
        bool flag = false;
        LL v_base = 1;
        for(LL i = 0; i < n; ++i){
            if(v_base > 1000) break;
            v_base *= base;
        }
        for(LL p = 2; p < v_base && p < 1000; ++p){
            if(divisible(v, base, p)){
                div.push_back(p);
                flag = true;
                break;
            }
        }
        if(!flag) return;
    }
}

void print_sample(LL v, vector<LL>& div){
    string bin;
    while(v > 0){
        bin.push_back('0' + (v&1));
        v /= 2;
    }
    reverse(bin.begin(), bin.end());
    cout << bin;
    for(int i = 0; i < div.size(); ++i){
        cout << " " << div[i];
    }
    cout << endl;
}

void solve(LL n, LL j){
    LL i = 0;
    for(LL i = 0; ; ++i){
        LL v = (1LL << (n-1)) + (i<<1) + 1;
        vector<LL> div;
        check(n, v, div);
        if(div.size() == 9){
            print_sample(v, div);
            --j;
            if(j <= 0) return;
        }
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL n, j;
        cin >> n >> j;
        cout << "case #" << t << ": " << endl;
        solve(n, j);
    }
    return 0;
}

