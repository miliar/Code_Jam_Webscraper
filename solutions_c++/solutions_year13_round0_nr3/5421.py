#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int checkPalindrome(int n)
{
	int copy = n, rev = 0;
	while (copy > 0)
	{
		rev = rev * 10 + (copy % 10);
		copy = copy/10;
	}
	if (rev == n)
		return 1;
	return 0;
}
int main()
{
	int a, b, i, count = 0, n, k, t, x;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (x = 0; x < t; x++)
	{
        cin >> a >> b;
        count = 0;
        for (i = a; i<=b; i++)
        {
            n = (int) sqrt(i);
            k = n*n;
            if(checkPalindrome(i) == 1 && checkPalindrome(n) == 1 && i == k)
            {
                 count++;
                 //cout << i << " " << n << endl;
            }
        }
        cout << "Case #"<<x+1<<": " << count << endl;
	}
	return 0;
}
