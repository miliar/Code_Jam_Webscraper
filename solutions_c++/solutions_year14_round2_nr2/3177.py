#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t, a, b, c, ch =0, g;
    int x, y;
    long long count;
    scanf("%d",&t);
    while(t--)
    {
        count = 0;
        ch++;
        scanf("%d %d %d",&a,&b,&c);
        for(int i = 0; i<(a); ++i)
        {
            x = i;
            for(int j = 0; j<(b); ++j)
            {
                y = j;
                g = x&y;
                for(int p = 0 ; p<c; ++p)
                {
                    if(g == p)
                    {
                        ++count;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %ld\n",ch,count);
    }
}
