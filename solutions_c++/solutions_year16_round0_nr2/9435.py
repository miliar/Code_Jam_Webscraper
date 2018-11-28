#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int T;
    char S[110];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s", S);
        int len = strlen(S), cnt = 0;
        while (1) {
            if (S[0] == '+') {
                int j = 1;
                while (j < len && S[j] == '+')
                    j++;
                if (j == len)
                    break;
                for (int i = 0; i < j; i++)
                    S[i] = '-';
            } else {
                int j = len-1;
                while (j && S[j] == '+')
                    j--;
                for (int i = 0; i <= j; i++) {
                    if (S[i] == '+')
                        S[i] = '-';
                    else
                        S[i] = '+';
                }
                for (int i = 0; i < j; i++, j--)
                    swap(S[i], S[j]);
            }
            cnt++;
        }
        printf("Case #%d: %d\n", t, cnt);
    }
}
