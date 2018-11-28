#include <iostream>
#include <cstdio>
#include <unordered_set>
using namespace std;

typedef long long LL;

unordered_set<LL> map1;
unordered_set<LL> map2;

void check(LL n, int& cnt) {
    map1.insert(n);
    while(n) {
        int tmp = n % 10;
        if(map2.find(tmp) == map2.end()) {
            cnt++;
            map2.insert(tmp);
        }
        n /= 10;
    } 
}


int main() {
    int T;
    LL n;
    cin >> T;
    int cas = 1;
    while(T--) {
        cin >> n;
        map1.clear();
        map2.clear();
        int cnt = 0;
        int ans = -1;
        LL plusn = n;
        while(1) {
            if(map1.find(n) != map1.end()) {
                break;
            }
            check(n, cnt);
            if(cnt == 10) {
                ans = n;
                break;
            }
            n += plusn;
        }
        cout << "Case #" << cas++ << ": ";
        if(ans == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << ans << endl;
    }
    return 0;
}



