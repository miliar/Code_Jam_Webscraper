#include <bits/stdtr1c++.h>
using namespace std;

#define int long long
bool seen[10];

#undef int
int main() {
    ios_base::sync_with_stdio(0);
#define int long long
    int t; cin >> t;
    for (int test=1; test<=t; test++) {
        for (int i=0; i<10; i++)
            seen[i] = false;
        int ans = 0;
        int n; cin >> n;
        if (n == 0) {
            cout << "Case #" << test << ": " << "INSOMNIA" << endl;
            continue;
        }
        int cnt = 0;
        int num = n;
        int i = 1;
        while (cnt < 10) {
            int tmp = 0;
            for (int j=0; j<10; j++) {
                tmp += seen[j];
            }
            cnt = tmp;
            if (cnt == 10)
                break;
            num = n*i++;
            tmp = num;
            while (tmp) {
                int rm = tmp%10;
                tmp /= 10;
                seen[rm] = true;
            }
        }
        cout << "Case #" << test << ": " << num << endl;
    }
}
