#include<cstdio>
#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string.h>
#include<string>
#include<algorithm>
#include<cmath>
#include<math.h>
#include<vector>
#include<list>
#include<ctime>
#include<cctype>
#include<deque>
#include<set>
#include<stack>
#include<queue>
#define LL long long int
using namespace std;

int N, M, mp[200][200];
int rowMax[200], columnMax[200], MM;

bool isIJOk(int i, int j)
{
    return (mp[i][j] == rowMax[i] || mp[i][j] == columnMax[j]);
}

int main(void)
{
    //freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
   // freopen("B-small-attempt5.in", "r", stdin);
  //  freopen("B-small-attempt5.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);


    int T, cas = 1; scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &N, &M);

        MM = 0;
        for (int i = 0; i < N; i++) rowMax[i] = 0;
        for (int j = 0; j < M; j++) columnMax[j] = 0;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                scanf("%d", &mp[i][j]);
                MM = max(MM, mp[i][j]);
                rowMax[i] = max(rowMax[i], mp[i][j]);
                columnMax[j] = max(columnMax[j], mp[i][j]);
            }
        }


        printf("Case #%d: ", cas++);

        if (MM > 100) {printf("NO\n"); continue;}

        bool flag = true;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (isIJOk(i, j) == false) {flag = false; break;}
            }
            if (flag == false) break;
        }

        if (flag == true)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }

    }


    return 0;
}
