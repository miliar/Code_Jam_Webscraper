#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int test;
    int i;

    scanf("%d", &test);
    for (i = 1; i <= test ; i++)
    {
        int a, b, k;
        int ii, jj;
        int sum = 0;

        scanf("%d %d %d", &a, &b, &k);
        for (ii = 0; ii < a; ii++)
            for (jj = 0; jj < b; jj++)
                if ((ii & jj) < k)
                    ++sum;
        cout << "Case #" << i << ": " << sum << endl;
    }

    return 0;
}
