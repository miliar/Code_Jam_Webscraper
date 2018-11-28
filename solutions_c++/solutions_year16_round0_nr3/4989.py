#include <iostream>
#include <string>
#include <set>
using namespace std;

set<string> myset;

int ans;
int T, N, J;
typedef long long LL;

bool check(string s) {
    LL son[11];
    for(int i = 2; i <= 10; i++) {
        LL tmp = 0;
        LL tmp2 = 1;
        for(int j = s.length()-1; j >= 0; j--) {
            tmp += (s[j]-'0') * tmp2;
            tmp2 *= i;
        }

        bool flag = false;
        for(LL j = 2; j*j <= tmp; j++) {
            if(tmp % j == 0) {
                son[i] = j;
                flag = true;
                break;
            }
        }
        if(!flag) return flag;
    }
    
    cout << s;
    for(int i = 2; i <= 10; i++) {
        cout << " " << son[i];
    }
    cout << endl;
    return true;
}


void dfs(string base) {
    if(ans == J) return;
    if(check(base)) {
        ans++;
    }
    for(int i = 1; i < base.size()-1; i++) {
        if(ans == J) return;
        string tmp = base;
        if(tmp[i] == '0')
            tmp[i] = '1';
        if(myset.find(tmp) == myset.end()) {
            myset.insert(tmp);
            dfs(tmp);
        }
    }
}

int main() {
    cin >> T;
    int cas = 1;
    while(T--) {
        ans = 0;
        myset.clear();
        cin >> N >> J;
        string base = "1" + string(N-2, '0') + "1";
        cout << "Case #" << cas++ << ":" << endl;
        myset.insert(base);
        dfs(base);
    }
    return 0;
}

