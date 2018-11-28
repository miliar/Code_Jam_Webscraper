#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        int n;
        char con[1010];
        scanf("%d%s", &n, con);

        int sum = con[0] - '0';
        int myMax = 0;
        for (int i = 1; i <= n; i++) {
            myMax = max(myMax, i - sum);
            sum += con[i] - '0';
        }
        
        printf("Case #%d: %d\n", times + 1, myMax);
    }
}
