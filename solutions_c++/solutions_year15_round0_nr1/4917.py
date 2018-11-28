#include <cstdio>
using namespace std;

int n;

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        int maxs;
        int standing = 0;
        int ans = 0;
        char input[2000] = "";

        scanf("%d", &maxs);
        scanf("%s", input);
        for (int j=0; j<=maxs; j++) {
            int num = input[j] - '0';
            
            if (num && j > standing) {
                ans += j - standing;
                standing += j - standing;
            }

            standing += num;
        }

        printf("Case #%d: %d\n", i+1, ans);
    }
}
