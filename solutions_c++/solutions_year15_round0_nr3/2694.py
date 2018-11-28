// RCC_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <algorithm>
#include <time.h>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int l, x;
        cin >> l >> x;
        string s;
        cin >> s;
        char curr = '1';
        bool sign = true;
        for (int i = 0; i < s.length(); ++i)
        {
            if (curr == '1')
                curr = s[i];
            else
            if (curr == 'i')
            {
                if (s[i] == 'i')
                {
                    curr = '1';
                    sign = !sign;
                }
                if (s[i] == 'j')
                {
                    curr = 'k';
                }
                if (s[i] == 'k')
                {
                    curr = 'j';
                    sign = !sign;
                }
            }
            else
            if (curr == 'j')
            {
                if (s[i] == 'i')
                {
                    curr = 'k';
                    sign = !sign;
                }
                if (s[i] == 'j')
                {
                    curr = '1';
                    sign = !sign;
                }
                if (s[i] == 'k')
                {
                    curr = 'i';
                }
            }
            else
            if (curr == 'k')
            {
                if (s[i] == 'i')
                {
                    curr = 'j';
                }
                if (s[i] == 'j')
                {
                    curr = 'i';
                    sign = !sign;
                }
                if (s[i] == 'k')
                {
                    curr = '1';
                    sign = !sign;
                }
            }
        }
        bool b = (curr == '1' && !sign && x % 2 == 1) || ((curr == 'i' || curr == 'j' || curr == 'k') && x % 4 == 2);
        string ss;
        if (x > 12)
            x = 12;
        for (int i = 0; i < x; ++i)
            ss += s;
        int counter = 0;
        curr = '1';
        sign = true;
        for (int i = 0; i < ss.length(); ++i)
        {
            if (curr == '1')
                curr = ss[i];
            else
            if (curr == 'i')
            {
                if (ss[i] == 'i')
                {
                    curr = '1';
                    sign = !sign;
                }
                if (ss[i] == 'j')
                {
                    curr = 'k';
                }
                if (ss[i] == 'k')
                {
                    curr = 'j';
                    sign = !sign;
                }
            }
            else
            if (curr == 'j')
            {
                if (ss[i] == 'i')
                {
                    curr = 'k';
                    sign = !sign;
                }
                if (ss[i] == 'j')
                {
                    curr = '1';
                    sign = !sign;
                }
                if (ss[i] == 'k')
                {
                    curr = 'i';
                }
            }
            else
            if (curr == 'k')
            {
                if (ss[i] == 'i')
                {
                    curr = 'j';
                }
                if (ss[i] == 'j')
                {
                    curr = 'i';
                    sign = !sign;
                }
                if (ss[i] == 'k')
                {
                    curr = '1';
                    sign = !sign;
                }
            }
            if (curr == 'i' && sign && counter == 0)
            {
                ++counter;
                curr = '1';
                continue;
            }
            if (curr == 'j' && sign && counter == 1)
            {
                ++counter;
                curr = '1';
                continue;
            }
        }
        cout << "Case #" << t + 1 << ": " << (counter == 2 && b ? "YES" : "NO") << endl;
    }
	return 0;
}

