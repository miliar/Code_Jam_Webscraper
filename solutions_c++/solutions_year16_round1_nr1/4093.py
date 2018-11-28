#include <iostream>

#include <cstdio>

#include <cstring>

using namespace std;



int main()
{
    int i, t, n, j, head;

    char maximum;
    char input[1001], output[2005];
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    for(i = 0; i<2004; i++)
    {
        output[i] = '\0';
    }

    scanf("%d\n",&t);

    for(i = 0; i <t; i++)
    {
        head = 1002;
        maximum = '\0';
        gets(input);
        n = strlen(input);
        for(j = 0; j < n; j++)
        {
            if(input[j] >= maximum)
            {
                output[head] = input[j];
                maximum = input[j];
                head--;
            }
            else
            {
                output[head + 1 + j] = input[j];
            }
        }

        printf("Case #%d: ",i+1);

        for(j = head+1; j < head + n + 1; j++)
        {
            printf("%c",output[j]);
            output[j] = '\0';
        }
        printf("\n");
    }

    return 0;
}
