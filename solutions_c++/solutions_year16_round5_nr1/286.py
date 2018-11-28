#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXL = 200000;

char tmp[MAXL];
char cur[MAXL];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%s", tmp);
        int L = strlen(tmp), curl = 0, answer = 0;

        for (int i = 0; i < L; ++i) {
            cur[curl++] = tmp[i];
            while (curl >= 2 && cur[curl - 1] == cur[curl - 2]) {
                answer += 10;
                curl -= 2;
            }
        }

        answer += (curl / 2) * 5;

        printf("Case #%d: %d\n", t + 1, answer);
    }

    return 0;
}
