#include <iostream>
#include <cmath>
using namespace std;

bool isPalindrome(int n)
{
    int num = n;
    int rev = 0;
    while (num != 0)
    {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return n == rev;
}

bool isPerfectSquare(int n)
{
    int closestRoot = (int) sqrt(n);
    return (n == closestRoot * closestRoot) && isPalindrome(closestRoot);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int a, b, ans = 0;
        cin >> a >> b;
        for (int j = a; j <= b; j++)
        {
            if (isPalindrome(j))
            {
                if (isPerfectSquare(j))
                    ans++;
            }
        }
        cout << "Case #" << i << ": " <<ans <<endl;
    }
}
