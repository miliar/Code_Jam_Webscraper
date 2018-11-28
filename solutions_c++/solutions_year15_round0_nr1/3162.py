#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


int n, numTest;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> numTest;
    int num = 0;
    while (numTest > 0)
    {
        cin >> n;
        string str;
        getline(cin, str);
        str.erase (0,1);
        int sum = 0;
        int res = 0;
        for (int i = 0; i <= n; i++)
        {
            if (sum < i)
            {
                res += i - sum;
                sum = i;
            }

            sum += (str[i] - '0');
            //cout << sum << "huhu" << endl;
        }
        cout << "Case #" << ++num <<": " <<  res << endl;
        numTest--;
    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
