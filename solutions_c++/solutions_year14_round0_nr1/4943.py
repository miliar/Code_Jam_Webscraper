#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define N 100

int a[N][N], b[N][N];

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("b.txt", "w", stdout);

    int T;
    int a1, a2;
    cin>>T;
    FOR(kk, 1, T)
    {
        cin>>a1;
        FOR(i, 1, 4)
        FOR(j, 1, 4)
        cin>>a[i][j];

        cin>>a2;
        FOR(i, 1, 4)
        FOR(j, 1, 4)
        cin>>b[i][j];

        int s = 0;
        int s2;
        FOR(i, 1, 4)
        FOR(j, 1, 4)
        if (a[a1][i] == b[a2][j])
        {
            s++;
            s2 = a[a1][i];
        }

        printf("Case #%d: ", kk);
        if (s == 1)
            printf("%d\n", s2);
        else if (s > 1)
            puts("Bad magician!");
        else
            puts("Volunteer cheated!");
    }

    //fclose(stdout);
    return 0;
}
