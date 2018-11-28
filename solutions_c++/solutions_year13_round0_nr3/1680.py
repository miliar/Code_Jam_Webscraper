#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

bool palindrome(long long a)
{
    int data[20];
    int n = 0;
    while (a != 0)
    {
        data[n++] = a%10;
        a = a/10;
    }
    for (int i = 0; i < n/2; i++)
    {
        if (data[i] != data[n-i-1]) return false;
    }
    return true;
}

int main()
{
     int count = 0;
     int t = 0;
     long long data[50];
     int n = 0;
     for (long long i = 1; i<= 10000000; i++)
         {
             if (palindrome(i))
                  if (palindrome(i*i))
                    {
                        data[n++] = i*i;
                    }
         }
     freopen("data.txt","r",stdin);
     freopen("ans.txt","w",stdout);
    /* for (int i = 0; i< n; i++)
     {
         cout << data[i] << endl;
     }*/
     scanf("%d",&t);
     while (t--)
     {
         count ++;
         long long a , b;
         cin >> a >> b;
         int ans = 0;
         for (int i = 0; i < n; i++)
         {
             if (data[i] >= a && data[i] <= b) ans ++;
         }
         //cout << a << ' ' << b << endl;
         printf("Case #%d: %d\n",count,ans);
     }
}
