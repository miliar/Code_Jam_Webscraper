#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <queue>
using namespace std;
const int N = 11050;
const int M = 5;

int mp[M][M];
int L, X;
char str[N];
int last[N];

void init()
{
    mp[1][1] = 1;
    mp[1][2] = 2;
    mp[1][3] = 3;
    mp[1][4] = 4;

    mp[2][1] = 2;
    mp[2][2] = -1;
    mp[2][3] = 4;
    mp[2][4] = -3;

    mp[3][1] = 3;
    mp[3][2] = -4;
    mp[3][3] = -1;
    mp[3][4] = 2;

    mp[4][1] = 4;
    mp[4][2] = 3;
    mp[4][3] = -2;
    mp[4][4] = -1;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    init();
    int t;
    scanf("%d", &t);
    for(int x=1; x<=t; x++)
    {
        scanf("%d%d", &L, &X);
        scanf("%s", str);
        for(int i=0; i<L; i++)
        {
            if(str[i] == 'i') str[i] = 2;
            if(str[i] == 'j') str[i] = 3;
            if(str[i] == 'k') str[i] = 4;
        }
        for(int i=1; i<X; i++)
        {
            for(int j=0; j<L; j++)
            {
                str[i*L+j] = str[j];
            }
        }
        str[X*L] = '\n';
        last[0] = str[0];
        for(int i=1; i<X*L; i++)
        {
            if(last[i-1] < 0)
                last[i] = -mp[-last[i-1]][str[i]];
            else last[i] = mp[last[i-1]][str[i]];
        }
        if(last[X*L-1] != -1)
        {
            printf("Case #%d: NO\n", x);
            continue;
        }
        bool flag = false;
        for(int i=0; i<X*L-2; i++)
        {
            for(int j=i+1; j<X*L-1; j++)
            {
                if(last[i] == 2 && last[j] == 4)
                {
                    flag = true;
                    break;
                }
            }
        }
        if(flag)
        {
            printf("Case #%d: YES\n", x);
        }
        else
        {
            printf("Case #%d: NO\n", x);
        }
    }
    return 0;
}
