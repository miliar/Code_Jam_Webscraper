#include <stdio.h>
#include <stdlib.h>

char * itoa(unsigned long n, char * str)
{
    for (int i = 0; i < 20; ++i)
    {
        if(n > 0)
        {
            str[i] = n%10 + 48;
            n = n/10;
        }
        else
        {
            str[i] = '\0';
        }
    }
}

bool palindrome(char * word, int length)
{
    if (length <= 1) return true;
    if (word[0] == word[length-1]) return palindrome(word+1, length-2);
    return false;
}

bool fair(unsigned long n)
{
    char number[20];
    int length = 0;
    itoa (n, number);
    for (int i = 0; i < 20 && length == 0; ++i)
    {
        if (number[i] == '\0')
        {
            length = i;
        }
    }
    return palindrome(number, length);
}

int main()
{
    int fairsquare[70], length = 0;
    for (int i = 0; i < 70; ++i)
    {
        fairsquare[i] = 0;
    }
    int t, a, b;
    scanf("%d", &t);
    for (unsigned long i = 1; i < 1e5; ++i)
    {
        if (fair(i) && fair(i*i))
        {
            fairsquare[length] = i*i;
            length++;
        }
    }
    for (int i = 0; i < t; ++i)
    {
        scanf("%d %d", &a, &b);
        int count = 0;
        for (int j = 0; j < length; ++j)
        {
            if (fairsquare[j] >= a && fairsquare[j] <= b)
            {
                count++;
            }
        }
        printf("Case #%d: %d\n", i+1, count);
    }
    return 0;
}