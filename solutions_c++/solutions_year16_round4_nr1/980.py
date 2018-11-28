#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

char ltr[] = {'P', 'R', 'S'};
int f[15], ff[15];

vector <int> prm, v;

void solve(int N, int f1, int f2, int f3, string s1, string s2, string s3)
{
    if(N == 0)
    {
        if(f1)  printf("%s\n", s1.c_str());
        if(f2)  printf("%s\n", s2.c_str());
        if(f3)  printf("%s\n", s3.c_str());
        return;
    }

    if(N % 2 == 1)
    {
        int vl = (1 << (N - 1)) / 3;

        if(f1 < f2 && f1 < f3)
            solve(N - 1, vl, vl, vl + 1, s1 + s2, s1 + s3, s2 + s3);
        else if(f2 < f1 && f2 < f3)
            solve(N - 1, vl, vl + 1, vl, s1 + s2, s1 + s3, s2 + s3);
        else
            solve(N - 1, vl + 1, vl, vl, s1 + s2, s1 + s3, s2 + s3);
    }

    if(N % 2 == 0)
    {
        int vl = (1 << (N - 1)) / 3;

        if(f1 > f2 && f1 > f3)
            solve(N - 1, vl + 1, vl + 1, vl, s1 + s2, s1 + s3, s2 + s3);
        else if(f2 > f1 && f2 > f3)
            solve(N - 1, vl + 1, vl, vl + 1, s1 + s2, s1 + s3, s2 + s3);
        else
            solve(N - 1, vl, vl + 1, vl + 1, s1 + s2, s1 + s3, s2 + s3);
    }
}

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        int N;
        scanf("%d", &N);
        int M = 1 << N;
        scanf("%d%d%d", &f[0], &f[1], &f[2]);
        ff[0] = f[0];
        ff[1] = f[1];
        ff[2] = f[2];
        sort(ff, ff + 3);

        if(ff[0] != M / 3 || ff[2] != M / 3 + 1)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }

        if(N % 2 == 1 && ff[1] != M / 3 + 1)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }

        if(N % 2 == 0 && ff[1] != M / 3)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }

        solve(N, f[1], f[0], f[2], "P", "R", "S");
    }

    return 0;
}
