#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;


long long a[10000000]; int br = 0; 
bool is_palindrome(long long pos)
{
    int pos2 = pos; 
    int rev = 0;
    
    while (pos2)
    {
        rev = rev*10 + pos2%10;
        pos2/=10; 
    }
    
    return pos == rev;
}


void magic()
{
    int i;
    long long temp;
    for (i = 1; i<= 10000002; i ++)
    {
        if (is_palindrome (i))
        {
            temp = (long long )i * i;
            if (is_palindrome(temp))
                a[br ++] = temp;
        }
    }
}

int solve ()
{
    long long F, L;
    cin >> F >> L;
    
    int l = upper_bound(a, a + br, L) - a;
    int f = lower_bound(a, a + br, F) - a;
    return l - f;
}


int main ()
{
    magic ();
     int t; 
    scanf ("%d", &t);
    
    int i; 
    for (i = 1; i <=t; i ++)
    {
        printf ("Case #%d: %d\n",i,  solve());
    }
    
    return 0;
}