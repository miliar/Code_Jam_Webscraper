#include <cstdio>

int main()
{
    int N;
    scanf("%d", &N);
    getchar();

    for(int n = 1; n <= N; ++n)
    {
        char c;
        bool first_time = true, minus_state = false;
        int moves = 0;

        while(c = getchar(), c != '\n')
        {
            if(c == '-' && !minus_state)
            {
                if(first_time)
                    moves++;
                else
                    moves += 2;

                minus_state = true;
            }
            else if(c == '+')
                minus_state = false;

            first_time = false;
        }

        printf("Case #%d: %d\n", n, moves);
    }

    return 0;
}
