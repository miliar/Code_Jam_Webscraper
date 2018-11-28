//#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tests;
    cin >> tests;
    for (int t = 1; t<=tests; t++)
    {
        string x;
        cin >> x;
        vector<char> vec;
        int c1 = 0, count = 0;
        for (int i = 0; i<x.length(); i++)
        {
            vec.push_back(x[i]);
            if (x[i] == '+')
                c1++;
        }
        while(c1 != x.length())
        {
            c1 = 0;
            bool flag = true;
            if (vec[0] == '-')
            {
                count++;
                for (int i = 0; i<vec.size(); i++)
                {
                    if (vec[i] == '+') break;
                        vec[i] = '+';
                }
            }
            for (int i = 0; i<vec.size(); i++)
            {
                if (vec[i] == '-')
                {
                    flag = false;
                }
            }
            if (flag == false)
            {
                count++;
                for (int i = 0; i<vec.size(); i++)
                {
                    if (vec[i] == '-') break;
                    vec[i] = '-';
                }
            }
            for (int i = 0; i<vec.size(); i++)
                if (vec[i] == '+') c1++;
        }
        cout << "Case #" << t << ": " << count << endl;
    }

    return 0;
}
