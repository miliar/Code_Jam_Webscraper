#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <limits>
#include <algorithm>

using namespace std;


bool res[10];


bool getres(long long f)
{
    if (f == 0)
        res[0] = 1;
    while (f > 0)
    {
        res[f % 10] = true;
        f /= 10;
    }
    for (int i = 0; i < 10; i++)
        if (!res[i])
            return false;
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);


    int n;
    long long f, tf, ans;

    cin >> n;


    for (int i = 0; i < n; i++)
    {
        cin >> f;
        memset(res, 0, 10);
        tf = 0;

        ans = -1;
        for (int j = 0; j < 8000; j++)
        {
            tf += f;
            if (getres(tf))
            {
                ans = tf;
                break;
            }
        }
        cout << "Case #" << to_string(i + 1) << ": ";
        if (ans != -1)
        {
            cout << ans << endl;
        }
        else
            cout << "INSOMNIA" << endl;
    }



    fclose(stdin);
    fclose(stdout);
    return 0;
}