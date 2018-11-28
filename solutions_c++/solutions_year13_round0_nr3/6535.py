#include <iostream>
#include <cmath>

using namespace std;

int Palin(int num)
{
    int n, digit, rev = 0;
    n = num;
    do
    {
        digit = num%10;
        rev = (rev*10) + digit;
        num = num/10;
    } while (num!=0);
    if (n == rev)
        return true;
    return false;
}

int main()
{
    int t;
    cin >> t;
    for (int z = 0; z < t; z++)
    {
        cout << "Case #" << (z+1) << ": ";
        int a, b;
        cin >> a >> b;
        int x = a, n = 0;
        while (x <= b)
        {
            if (sqrt(x) == (int)sqrt(x) && Palin(x) && Palin(pow(x, .5)))
            {
                n++;
            }
            x++;
        }
        cout << n << endl;
    }
}
