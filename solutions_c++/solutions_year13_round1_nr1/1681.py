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
        int curr = 0;
        int counter = 0;
        for(int j=r+1; ; j+=2)
        {
            curr = 2*j-1;
            if(curr<=t)
            {
                t = t - curr;
                counter++;
            }
            else
                break;
        }
        printf("Case #%d: %d\n", i, counter);
    }
    return 0;
}
