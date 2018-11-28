#include <bits/stdc++.h>

/*
ZERO Z 1*x0
ONE
TWO W
THREE
FOUR
FIVE
SIX X
SEVEN V
EIGHT
NINE

0123456789
EFHIORSTUX


*/

char number[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char buffer[2048];
int tmp[256];
int count[256];
char prt[2048];



int cnt = 0;
int l = 0;

inline bool test()
{
    for (int i = 'A'; i <= 'Z'; i++)
       if (count[i] < tmp[i])
       {
//           printf("err %d %d %d\n", i, count[i], tmp[i]);
           return false;
       }
    return true;
}

inline bool check(int x)
{
    memset(tmp, 0, sizeof tmp);
    for (int i = 0; number[x][i]; i++)
        tmp[number[x][i]]++;
//    for (int i = 'A'; i <= 'Z'; i++) printf("%d ", tmp[i]);
//        puts("__");
    if (test())
    {
//        printf("ok %d\n", x);
        for (int i = 'A'; i <= 'Z'; i++)
        {
            count[i] -= tmp[i];
            l -= tmp[i];
        }
        return true;
    }
    return false;
}

inline void uncheck(int x)
{
    memset(tmp, 0, sizeof tmp);
    for (int i = 0; number[x][i]; i++)
        tmp[number[x][i]]++;
    for (int i = 'A'; i <= 'Z'; i++)
        {
            count[i] += tmp[i];
            l += tmp[i];
        }

}


bool dfs(int k)
{
//    printf("%d\n", l);
    if ( l == 0) return true;
    for (int i = k; i < 10; i++)
    {
        if (check(i))
        {
//            printf("l = %d\n",l);
            if (dfs(i))
            {
                prt[cnt++] = '0' + i;
                return true;
            }
            else
            {
                uncheck(i);
            }
        }

    }
    return false;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T_T, __ = 0;
    scanf("%d", &T_T);

    while (T_T--)
    {
        printf("Case #%d: ", ++__);
        scanf("%s", buffer);

        memset(count, 0, sizeof count);

        l =  strlen(buffer);

        cnt = 0;

        for (int i = 0; buffer[i] ; i++)
            count[buffer[i]]++;
//        for (int i = 'A'; i <= 'Z'; i++) printf("%d ", count[i]);
//        puts("");

        dfs(0);

        prt[cnt]=0;
        std::reverse(prt, prt + cnt);
        puts(prt);
    }



    return 0;
}
