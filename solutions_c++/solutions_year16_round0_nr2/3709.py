#include <bits/stdc++.h>

using namespace std;
char line[1000];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    int T,N,steps;
    scanf("%d\n",&T);
    for(int test = 1; test <= T; ++test)
    {
        steps = 0;
        memset(line,0,sizeof(line));
        scanf("%s",line + 1);
        line[0] = line[1];
        N = strlen(line);
        int poz = 1;
        while(1)
        {
            while(poz < N && line[poz] == line[poz-1])
                ++poz;
            if(poz == N)
            {
                if(line[poz-1] == '-')
                    ++steps;
                printf("Case #%d: %d\n",test,steps);
                break;
            }
            line[poz-1] = line[poz];
            ++steps;
        }
    }

    return 0;
}
