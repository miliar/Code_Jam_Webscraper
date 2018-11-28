#include <bits/stdc++.h>
using namespace std;
#define MAX 5005
#define ll long long

int fn();
char arr1[MAX], arr2[5 * MAX];

int main()
{
     freopen("A-large.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int tc, cases = 1;

    scanf("%d", &tc);
    while(tc--)
    {
        scanf("%s", arr1);
        int l = strlen(arr1);

        int start = fn();

        printf("Case #%d: ",cases++);

        for(int i = start; i < start + l; i++)
            printf("%c", arr2[i]);

        printf("\n");
    }

    return 0;
}

int fn()
{
    int start = 2000;
    int e = start + 1;

    arr2[start] = arr1[0];

    int l = strlen(arr1);
    for(int i = 1; i < l; i++)
    {
        if(arr1[i] > arr2[start])
        {
            arr2[start - 1] = arr1[i];
            start--;
        }
        else if(arr1[i] < arr2[start])
        {
            arr2[e] = arr1[i];
            e++;
        }
        else
        {
            if(arr2[e - 1] > arr1[i])
            {
                arr2[e] = arr1[i];
                e++;
            }
            else
            {
                arr2[start - 1] = arr1[i];
                start--;
            }
        }
    }

    return start;
}
