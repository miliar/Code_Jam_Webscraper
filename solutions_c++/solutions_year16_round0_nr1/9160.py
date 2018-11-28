//#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tests;
    cin >> tests;
    long long num, c, temp, t2;
    for (int t = 1; t<=tests; t++)
    {
        c = 0;
        bool arr[11] = {};
        bool flag = true;
        cin >> num;
        temp = num;
        if (num == 0)
        {
            flag = false;
            goto answer;
        }
        while(temp <= powl(10, 9))
        {
            flag = true;
            c++;
            temp = c*num;
            t2 = temp;
            while (t2 != 0)
            {
                int x = t2%10;
                arr[x] = true;
                t2/=10;
            }
            for (int i = 0; i< 10; i++)
            {
                if (arr[i] == false) break;
                if (i == 9)
                {
                    goto answer;
                }
            }
            flag = false;
        }
answer:
        if (flag == true) cout << "Case #" << t << ": " << temp << endl;
        else
            cout << "Case #" << t << ": INSOMNIA" << endl;
    }


    return 0;
}
