#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int mark[20];
int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%d", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", Case);
            continue;
        }
        
        for(int i = 0; i <= 9; ++i) mark[i] = 0;
        for(int i = 1; ; i++)
        {
            int now = n * i;
            while(now)
            {
                int k = now % 10;
                now /= 10;
                ++mark[k];
            }
            
            bool ok = 1;
            for(int i = 0; i <= 9; ++i) if(!mark[i]) {ok = 0; break;}
            if(ok)
            {
                printf("Case #%d: %d\n", Case, i * n);
                break;
            }
        }
    }
    return 0;
}