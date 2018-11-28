#include <cstdio>
#include <cstring>

int K, N;
int start[200];

int open[20];
int chest[20][200];

int backtrack[1<<20];
int front, back;
int queue[1<<20];

int main()
{
    int nprob;

    scanf("%d", &nprob);
    for (int prob = 0; prob < nprob; prob++) {
        memset(start, 0, sizeof(start));
        memset(chest, 0, sizeof(chest));

        scanf("%d%d", &K, &N);
        for (int i = 0; i < K; i++) {
            int x; 
            scanf("%d", &x); x--;
            start[x]++;
        }
        for (int i = 0; i < N; i++) {
            scanf("%d%d", &open[i], &K); open[i]--;
            while (K--) {
                int x;
                scanf("%d", &x); x--;
                chest[i][x]++;
            }
        }

        memset(backtrack, -1, sizeof(backtrack));
        front = back = 0;

        backtrack[0] = 0;
        queue[back++] = 0;

        while (front < back) {
            int state = queue[front++];

            for (int i = 0; i < N; i++) {
                int nstate = state ^ (1<<i);

                if ((state & (1<<i)) == 0 && backtrack[nstate] < 0) {
                    int n = start[open[i]];

                    for (int c = 0; c < N; c++)
                        if ((state & (1<<c)) == (1<<c)) {
                            if (open[c] == open[i]) n--;
                            n += chest[c][open[i]];
                        }
                    if (n > 0) {
                        backtrack[nstate] = i;
                        queue[back++] = nstate;
                    }
                }
            }
        }

        printf("Case #%d:", prob+1);
        if (backtrack[(1<<N)-1] < 0)
            printf(" IMPOSSIBLE\n");
        else {
            int path[20];
            int state = (1<<N)-1;

            for (int i = N-1; i >= 0; i--) {
                path[i] = backtrack[state];
                state ^= 1 << backtrack[state];
            }
            for (int i = 0; i < N; i++) printf(" %d", path[i]+1);
            printf("\n");
        }
    }

    return 0;
}
