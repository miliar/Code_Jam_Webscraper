#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

bool isPal(int x)
{
    int i, j, len;
    char buffer [33];
    itoa(x,buffer,10);
    for(i = 0; buffer[i]; i++);
    len = i;
    for(i = 0, j = (len - 1); i < len; i++, j--)
        if(buffer[i] != buffer[j])
            return false;
    return true;
}

int main()
{
    //freopen("three.in", "r", stdin);
    //freopen("three.out", "w", stdout);
    int n, i, j, k, a, b, t, T;
    cin >> T;
    for(t = 1; t <= T; t++)
    {
        n = 0;
        cin >> a >> b;
        for(i = a; i <= b; i++)
        {
            int x = (int)sqrt(i);
            if(isPal(i) && isPal(x) & (x*x == i))
                n++;
        }
        cout << "Case #" << t << ": " << n << "\n";
    }


    return 0;
}
