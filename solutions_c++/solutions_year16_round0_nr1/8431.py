#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;
const int maxn = 10007;

int vis[20];
long long n;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int test_case;
    scanf("%d", &test_case);
    int case_num = 0;
    while (test_case--) {
        cin >> n;
        case_num++;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", case_num);
        }
        else {
            int flag = 0;
            memset(vis, 0, sizeof(vis));
            long long k = 1;
            long long s = 0;
            long long ans = 0;
            while (k <= maxn) {
                s = n * k;
                ans = n * k;
                while (s) {
                    int temp = s % 10;
                    s = s / 10;
                    if (!vis[temp]) {
                        vis[temp] = 1;
                        flag++;
                    }
                }
                if (flag == 10) {
                    break;
                }
                k++;
            }
            if (flag == 10) {
                cout << "Case #" << case_num << ": " << ans << endl;
            }
            else {
                cout << "Case #" << case_num << ": INSOMNIA" << endl;
            }
        }
    }
    return 0;
}
