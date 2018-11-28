#include<iostream>
#define s(n) scanf("%d",&n)

int main(void)
{
    int t, c, i, j, a, b , k, cnt,x;
    s(t);
    c=1;
    while(c<=t)
    {
        cnt=0;
        s(a);s(b);s(k);

        for(i=0; i<a; i++)
        {
            for(j=0;j<b;j++)
            {
                x=i&j;
                if(x < k)
                    cnt++;
            }
        }

        printf("Case #%d: %d\n", c, cnt);
        c++;
    }
}
