#include <cstdio>
#include <cstdlib>

using namespace std;

bool flag[10];

bool check()
{
    for(int i = 0; i < 10; i++)
        if(!flag[i])
            return false;
    return true;
}

void count(int n)
{
    int k = n;
    while(k > 0)
    {
        flag[k % 10] = true;
        k /= 10;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        int n;
        scanf("%d", &n);

        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        //reset
        for (int i = 0; i < 10; ++i)
        {
            flag[i] = false;
        }

        int now = 0;

        while(!check())
        {
            now += n;
            count(now);
        }

        printf("Case #%d: %d\n", t, now);

    }

}