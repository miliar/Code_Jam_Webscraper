#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    int test_case ,counter  ;
    long long int multiplier , current_step , N , true_multiplier;

    scanf("%d", &test_case);

    for(int i = 0 ; i < test_case ;i++)
    {
        bool marker[10];
        for(int j = 0 ; j < 10 ; j++)
        {
            marker[j] = false;
        }
        counter = 0;

        scanf("%lld", &N);
        true_multiplier = -1;
        if(N == 0)
        {
            printf("Case #%d: INSOMNIA\n", i+1);
        }
        else
        {
            multiplier = 1;
            while(counter < 10)
            {
                current_step = N * multiplier;
                while(current_step != 0)
                {
                    if(marker[current_step%10] == false)
                    {
                        counter++;
                        marker[current_step%10] = true;
                        if(counter == 10)
                        {
                            true_multiplier = multiplier;
                            current_step = 0;
                            break;
                        }
                    }
                    current_step /=10;
                }
                multiplier++;
            }
            printf("Case #%d: %lld\n", i+1 , N*true_multiplier);
        }
    }
    return 0;
}
