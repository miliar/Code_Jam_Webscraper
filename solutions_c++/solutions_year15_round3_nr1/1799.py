#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int numTest;
    cin >> numTest;
    int num = 0;
    int m, n, w, temp, res;
    while (numTest > 0)
    {
        cin >> m >> n >> w; res = 0;
        if (w == 1) res = m * n;
        else if (w == n) res = m - 1 + w;
        else
        {
            temp = n / w;
            if (n % w == 0)
            {
                res = m * (temp - 1 + w);
            }
            else
            {
                res = temp * (m - 1);
                res += temp + w;
            }
        }
        cout << "Case #" << ++num <<": " <<  res << endl;
        numTest--;
    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
