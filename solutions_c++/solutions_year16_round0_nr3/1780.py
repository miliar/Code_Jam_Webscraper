#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int modlist[] = {0,0,3,7,3,3,7,3,3,7,3};

bool test(string s) {
    int len = s.length();
    int baselist[] = {2,4,3,6,9};
    for(int k = 0; k < 5; k ++) {
        int base = baselist[k];
        int mod = modlist[base];
        int val = 0, mul = 1;
        for(int i = len - 1; i >= 0; i --) {
            val = (val + (s[i] - '0') * mul) % mod;
            mul = mul * base % mod;
        }
        if(val) return false;
    }
    return true;
}
int cnt = 0;
void dfs(string s) {
    int n = s.length();
    if(n == 31) {
        s.push_back('1');
        if(test(s)) {
            cout << s;
            for(int base = 2; base <= 10; base ++) {
                printf(" %d", modlist[base]);
            }
            cout << endl;
            cnt ++;
        }
    } else {
        dfs(s + "0");
        if(cnt == 500) return ;
        dfs(s + "1");
    }
}

int main() {
    freopen("C.out", "w", stdout);
    printf("Case #1:\n");
    dfs("1");
    return 0;
}
