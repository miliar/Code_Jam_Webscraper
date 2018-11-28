#include <iostream>
#include <cstdio>

using namespace std;

int tab[1100000];
int lim = 1100000-1;

int solve(int v) {
    //if (tab[v] != -2) return tab[v];
    //if (2*v <= )
    bool found[10];
    for (int i = 0; i < 10; i++)
        found[i] = false;

    int MAXITER = 1000000;
    for (int i = 1; i < MAXITER; i++)
    {
        int l = v*i;
        while (l > 0) {
            found[l%10] = true;
            l /= 10;
        }
        bool good = true;
        for (int k = 0; k < 10; k++) {
            if (!found[k]) good = false;
        }
        if (good)
            return tab[v] = i;

    }
    return tab[v]=-1;

}

int main()
{
    for (int i = 0; i <= lim; i++)
        tab[lim] = -2;
    /*for (int i = 0; i <= lim; i++)
        solve(i);*/

    fprintf(stderr, "DOPOCITANO\n");


    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
            int N;
            scanf("%d", &N);
            int v = solve(N) * N;
            if (v > 0) {
                printf("Case #%d: %d\n", t+1, v);
            }
            else {
                printf("Case #%d: INSOMNIA\n", t+1);
            }

    }
    return 0;
}
