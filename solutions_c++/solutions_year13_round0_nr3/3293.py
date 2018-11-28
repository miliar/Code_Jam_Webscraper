#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;


int main()
{
    int t, cas, palin, i;

    int arr[5] = {1, 4, 9, 121, 484};

    int A,B;

    scanf("%d", &t);
    cas = 0;

    while(t--)
    {
        cas++;
        scanf("%d%d", &A, &B);
        palin = 0;

        for(i=0;i<5;i++)
        {
            if((arr[i]>=A) && (arr[i]<=B))
                palin++;
        }

        printf("Case #%d: %d\n", cas, palin);
    }

	return 0;
}
