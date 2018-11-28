#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int T;
long long N;
long long n;
long long temp;
long long  MAP[10];

bool check()
{
    for(int i=0;i<=9;i++)
    {
        if(MAP[i] == 0)
            return false;
    }
    return true;
}

int main()
{
    freopen("/Users/dingning/Desktop/VJ/A-large.in", "r", stdin);
    freopen("/Users/dingning/Desktop/VJ/out.txt","w",stdout);

    int kase = 1;
    scanf("%d",&T);
    while(T--)
    {
        memset(MAP, 0, sizeof(MAP));
        cin>>n;
        long long temp2 = n;
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n",kase++);
        }
        else
        {
            while(!check())
            {
                N = n;
                while(N != 0)
                {
                    temp = N % 10;
                    MAP[temp] = 1;
                    N/=10;
                }
                n += temp2;
            
            }
            printf("Case #%d: %lld\n",kase++,n-temp2);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

