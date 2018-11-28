#include<iostream>
#include<set>
#include<cstring>
#include<cstdio>

using namespace std;
bool visited[10];

bool fillarr(long long num)
{
    while(num)
    {
        visited[num%10] = 1;
        num = num/10;
    }

    for(int i=0; i<10; i++)
        if(visited[i]==0)
            return 0;

    return 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large_output.out", "w", stdout);
    int cases;
    long long n, num;
    cin>>cases;

    for(int ca=1; ca<=cases; ca++)
    {
        bool done = 0;
        int mul = 1;
        memset(visited, 0, sizeof(visited));
        cin>>n;
        num = n;

        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n", ca);
            continue;
        }

        while(!done)
        {
            done = fillarr(num);
            if(!done)
            {
                mul++;
                num = mul * n;
            }
        }

        printf("Case #%d: %lld\n", ca, num);
    }

    return 0;
}

