#include<stdio.h>
#include<vector>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("large_output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int _t = 1; _t <= t; _t++)
    {
        long long x;
        scanf("%lld", &x);
        printf("Case #%d: ", _t);
        if(x == 0) printf("INSOMNIA\n");
        else
        {
            std::vector<bool> isvalid(10, 0);

            for(int i = 0; ; i++)
            {
                for(long long y = x * i; y != 0; y /= 10)
                    isvalid[y % 10] = true;

                bool isallvalid = true;

                for(int i = 0; i < 10; i++)
                    if(!isvalid[i])
                    {
                        isallvalid = false; break;
                    }

                if(isallvalid)
                {
                    printf("%lld\n", x * i);
                    break;
                }
            }
        }
    }
}
