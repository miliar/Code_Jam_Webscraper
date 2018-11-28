#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

const int MXN = 16;
int r, c;
int n;
int other[MXN * 10];

char draw[MXN][MXN+1];

int dx[]={0, -1, 0, 1};
int dy[]={1, 0, -1, 0};

bool solve()
{
    int s = r*c;
    for (int i=0; i<(1<<s); i++)
    {
        bool good = true;
        for (int j=0; j<n; j++)
        {
            if (other[j] < j) continue;
            int x, y, d;
            if (j < c) {
                d = 0;
                x = j;
                y = 0;
            } 
            else if (j < c + r)
            {
                d = 1;
                x = c-1;
                y = j - c;
            }
            else if (j < c + r + c)
            {
                d = 2;
                x = c - 1 - (j - c -r);
                y = r - 1;
            }
            else
            {
                d = 3;
                x = 0;
                y = r - 1 - (j - c -r -c);
            }
            while (x >= 0 && y >= 0 && x < c && y < r)
            {
                int bid = x + y * c;
                if (i & (1<<bid))
                {
                    d ^= 3;
                }
                else
                {
                    d ^= 1;
                }
                x += dx[d];
                y += dy[d];
            }
            int id = - 1;
            switch (d)
            {
            case 0: id = r + c + c-1 - x; break;
            case 1: id = 2 * r + 2* c -1 - y; break;
            case 2: id = x; break;
            case 3: id = c + y; break;
            }
            if (id != other[j]) {
                good = false;
                break;
            }
        }


        if (good)
        {
            memset(draw, 0, sizeof(draw));
            for (int j=0; j<s; j++) {
                draw[j/c][j%c] = (i&(1<<j)) ? '\\' : '/';
            }
            return true;
        }
    }
    return false;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i=1; i<=t; i++)
    {
        scanf("%d %d", &r, &c);
        n = 2 * (r+c);
        for (int i=0; i<n/2; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            a--; b--;
            other[a] = b;
            other[b] = a;
        }
        printf("Case #%d:\n",i);
        if (solve())
        {
            for (int i=0; i<r; i++) puts(draw[i]);
        }
        else
        {
            puts("IMPOSSIBLE");
        }
    }
}
