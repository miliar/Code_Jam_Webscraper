using namespace std;
#include <bits/stdc++.h>
#define fto(i, l, r) for(int i = l; i <= r; ++i)
#define maxN 1005
int a[maxN], n, cnt, ans;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTest;
    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d ", &n);
        fto(i, 0, n) {
            scanf("%c", &a[i]);
            a[i]-=48;
        }
        //scanf("\n");

        cnt = ans = 0;
        fto(i, 0, n) {
            if (cnt < i) {
                ans += i-cnt;
                cnt = i;
            }
            cnt+=a[i];
        }
        printf("Case #%d: %d\n", iTest, ans);
    }
}
