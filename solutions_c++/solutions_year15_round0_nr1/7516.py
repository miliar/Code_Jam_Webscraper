#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    char array[1024] = {0};
    int T = 0;

    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
    {
        int max = 0;
        int ppl = 0;

        scanf("%d", &max);
        scanf("%s", array);

        int sum = array[0] - '0';
        for (int j = 1; j <= max; j++)
        {
            if (sum >= j)
                sum += array[j] - '0';
            else
            {
                int minus = j - sum;
                ppl += minus;
                sum += minus + (array[j] - '0');
            }
        }
        cout << "Case #" << i << ": " << ppl << endl;
    }
}
