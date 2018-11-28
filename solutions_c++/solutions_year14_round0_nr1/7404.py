#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

void got(int a[4][4])
{
     for (int i = 0; i < 4; i++)
         for (int j = 0; j < 4; j++)
             scanf("%d", &a[i][j]);
}

bool check(int b[4][4], int k, int x)
{
     for (int i = 0; i < 4; i++)
         if (b[k][i] == x) return true;
     return false;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int i, ans, ts, ks, a1, b1;
    int a[4][4], b[4][4];
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        scanf("%d", &a1);
        got(a);
        scanf("%d", &b1);
        got(b);
        int cnt = 0;
        for (i = 0; i < 4; i++){
            if (check(b, b1 - 1, a[a1 - 1][i])) { cnt++; ans = a[a1 - 1][i]; }
        }
        printf("Case #%d: ", ks + 1);
        if (cnt == 0)
           printf("Volunteer cheated!");
        if (cnt == 1)
           printf("%d", ans);
        if (cnt > 1)
           printf("Bad magician!");
        printf("\n");
    }
    return 0;
}
