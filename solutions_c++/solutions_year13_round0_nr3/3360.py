#include <iostream>
#include <cstdio>
#include <cstdlib>
#
using namespace std;


int main()
{
    int t, cas_no, result, i;

    int numbers[5] = {1, 4, 9, 121, 484};

    int A,B;

    scanf("%d", &t);
    cas_no = 0;

    while(t--)
    {
        cas_no++;
        scanf("%d%d", &A, &B);
        result = 0;

        for(i=0;i<5;i++)
        {
            if((numbers[i]>=A) && (numbers[i]<=B))
                result++;
        }

        printf("Case #%d: %d\n", cas_no, result);
    }

	return 0;
}
