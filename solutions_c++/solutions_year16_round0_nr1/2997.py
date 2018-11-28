#include<iostream>
#include<cstring>
using namespace std;

bool mark[10];
int main() {
    int T;
    cin >> T;
    int n;
    for(int cas = 1; cas <= T; cas++) {
        memset(mark, false, sizeof(mark));
        cin >> n;
        if(!n) {
            cout << "Case #" << cas << ": INSOMNIA\n";
            continue;
        }
        int remain = 10;
        int m = n, t, tt;
        while(remain) {
            t = m;
            while(t) {
                tt = t%10;
                if(!mark[tt]) {
                    mark[tt] = true;
                    remain--;
                }
                t /= 10;
            }
            m += n;
        }
        cout << "Case #" << cas << ": " << m-n << "\n";
    }
}
