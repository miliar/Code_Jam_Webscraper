#include<iostream>
#include<cstring>
using namespace std;

char s[110];

void flip(int n) {
    for(int i = 0; i <= n/2; i++) swap(s[i], s[n-i]);
    for(int i = 0; i <= n; i++) s[i] = (s[i]=='+' ? '-' : '+');
}

int main() {
    int T;
    cin >> T;
    int n;
    for(int cas = 1; cas <= T; cas++) {
        cin >> s;
        int ans = 0;
        int p1, p2;
        bool ok = false;
        while(1) {
            for(p1 = 0; p1 < strlen(s); p1++) {
                if(s[p1] == '-') break;
            }
            if(p1 == strlen(s)) {
                break;
            }
            else if(p1) {
                for(int i = 0; i < p1; i++) s[i] = '-';
                ans++;
            }
            for(int i = strlen(s)-1; i >= 0; i--) {
                if(s[i] == '-') {
                    flip(i);
                    ans++;
                    break;
                }
            }
        }
        cout << "Case #" << cas << ": " << ans << "\n";
    }
}
