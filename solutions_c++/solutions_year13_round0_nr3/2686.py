#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int isPalindrome(long long int i);

int main()
{
    long long int A;
    long long int B;
    long long int i;
    long long int k;
    long long int count = 0;

    int T;
    int j;

    scanf("%d", &T);

    for(j = 1; j <= T; j++)
    {
        count = 0;
        scanf("%Ld", &A);
        scanf("%Ld", &B);

        for(i = A; i <= B; i++)
        {
            if(isPalindrome(i) == 0)
            {
                k = (long long int) sqrt((double)i);
               
                if(k * k == i)
                {
                    if(isPalindrome(k) == 0)
                        count++;
                }
            }

        }

        printf("Case #%d: %Ld\n", j, count);
    }
    return 0;
}

int isPalindrome(long long int i)
{
    char array[30];
    int j = 0;
    int k = 0;
    int boo = 0;
  
    array[j] = i%10;

    while((i = i/10) != 0)
    {
        array[++j] = i % 10;
    }

    for(k = 0; k <= j/2; k++)
    {
        if(array[k] != array[j-k])
        {
            boo = 1;
            break;
        }
    }
    
    return boo;
}
