#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1000;

int n;
double a[N];
double b[N];
bool map[N][N];
int result[N];
bool state[N];

bool find(int a)
{
    for (int i = 0; i < n; i++) {
        if (map[a][i] && !state[i]) {
            state[i] = true;
            if (result[i] == -1 || find(result[i])) {
                result[i] = a;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &a[i]);
        }
        sort(a, a + n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &b[i]);
        }
        sort(b, b + n);

        //deceitful
        for (int i = 0; i < n; i++) {
            result[i] = -1;
            for (int j = 0; j < n; j++) {
                map[i][j] = a[i] > b[j];
            }
        }
        int score_d = 0;
        for (int i = 0; i < n; i++) {
            memset(state, 0, sizeof(bool)*n);
            if (find(i)) {
                score_d++;
            }
        }

        //honest
        int score_h = 0;
        for (int i = 0; i < n; i++) {
            bool win = true;
            for (int j = 0; j < n; j++) {
                if (b[j] > a[i]) {
                    b[j] = -1.0;
                    win = false;
                    break;
                }
            }
            if (win) {
                score_h ++;
            }
        }
        printf("Case #%d: %d %d\n", cs, score_d, score_h);
    }
    return 0;
}
