#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int test;
    scanf("%d", &test);
    for(int i=1; i<=test; i++)
    {
        int r, t;
        scanf("%d%d", &r, &t);
        int cur = 0;
        int count = 0;
        int j;
        for(j=r+1; ; j+=2)
        {
            cur = 2*j-1;
            if(cur<=t)
            {
                t = t - cur;
                count++;
            }
            else
                break;
        }
        printf("Case #%d: %d\n", i, count);
    }
    return 0;
}
