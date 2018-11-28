#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <cstring>
using namespace std;
#define MAX 20
#define ll int

void fn(int i, int j, int left, int with);

bool array[MAX][MAX];
int ans, cases, p = 1, r, c;
const int inf = 9999999;

int main()
{
    int left;
    memset(array, 0, sizeof(array));
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("c.out", "w", stdout);


    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d %d %d", &r, &c, &left);
        ans = inf;
        fn(0, 0, left, 0);
        printf("Case #%d: %d\n", p++, ans);

    }

    return 0;
}

void fn(int i, int j, int left, int with)
{
    if(left == 0)
        ans = min(ans, with);

    if(i == r)
        return;

    if(j == c)
        return fn(i + 1, 0, left, with);

    ///dont put
    fn(i, j + 1, left, with);

    ///put
    array[i][j] = 1;

    int tmp = 0;
    if(i > 0 && array[i - 1][j])
        tmp++;

    if(j > 0 && array[i][j - 1])
        tmp++;

    fn(i, j + 1, left - 1, with + tmp);

    array[i][j] = 0;

    return ;
}





