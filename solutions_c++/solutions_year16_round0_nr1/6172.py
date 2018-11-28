#include <cstdio>
#include <bitset>

using namespace std;

int main()
{
    int N, T;
    scanf("%d", &T);

    for(int t = 1; t <= T; ++t)
    {
        scanf("%d", &N);

        if(N)
        {
            bitset<10> bits;
            int mul = 1;
            int last_num = -1;
            while(bits.count() != 10)
            {
                int n = mul*N;
                last_num = n;
                while(n)
                {
                    bits.set(n - (n/10)*10);
                    n /= 10;
                }

                mul++;
            }

            printf("Case #%d: %d\n", t, last_num);
        }
        else
            printf("Case #%d: INSOMNIA\n", t);
    }

    return 0;
}
