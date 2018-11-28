#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>

using namespace std;

typedef struct {
    int x;
    int y;
    int height;
} coordi;

int main()
{
    int T, i, j, k, M, N, tmp, res;
    int a[100][100];
    int checked[100][100];
    multimap<int, coordi> sorted_grass;
    multimap<int, coordi>::iterator it;
    scanf("%d", &T);

    coordi tmp2;
    for (i = 0; i < T; i++)
    {
        sorted_grass.clear();
        memset(a, 0, sizeof(a));
        memset(checked, 0, sizeof(checked));
        scanf("%d", &N);
        scanf("%d", &M);
        for (j = 0; j < N; j++)
        {
            for (k = 0; k < M; k++)
            {
                scanf("%d", &tmp);
                a[j][k] = tmp;
                tmp2.x = j;
                tmp2.y = k;
                tmp2.height = tmp;
                sorted_grass.insert( pair<int, coordi>(tmp, tmp2) );
            }
        }
        for (it=sorted_grass.begin(); it!=sorted_grass.end(); ++it)
        {
            // std::cout << (*it).first << '\n';
            tmp2 = (*it).second;
            // printf("tmp2.x = %d, tmp2.y = %d, tmp2.height = %d\n", tmp2.x, tmp2.y, tmp2.height);
            if (checked[tmp2.x][tmp2.y] == 0)
            {
                checked[tmp2.x][tmp2.y] = 1;
                res = 1;
                for (j = 0; j < N; j++)
                {
                    if (a[j][tmp2.y] > tmp2.height)
                    {
                        res = 0;
                        break;
                    }
                    else
                        checked[j][tmp2.y] = 1;
                }
                if (res == 0)
                {
                    res = 1;
                    for (j = 0; j < M; j++)
                    {
                        if (a[tmp2.x][j] > tmp2.height)
                        {
                            res = 0;
                            break;
                        }
                        else
                            checked[tmp2.x][j] = 1;
                    }
                }
                if (res == 0)
                {
                    printf("Case #%d: NO\n", i + 1);
                    break;
                }
            }
        }
        if (res == 1)
            printf("Case #%d: YES\n", i + 1);

    }
    return 0;
}
