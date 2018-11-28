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


    int cases, ans;
    cin >> cases;

    string str;

    for (int t = 0; t < cases; t++)
    {
        cin >> str;
        ans = 0;

        for (size_t i = 0; i < str.length(); i++)
        {
            if (i != 0 && str[i] != str[i - 1])
                ans++;
        }
        
        if (str.back() == '-')
            ans++;

        cout << "Case #" << to_string(t + 1) << ": " << ans << endl;
        
    }
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}