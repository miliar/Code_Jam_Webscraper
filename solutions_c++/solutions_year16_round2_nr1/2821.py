#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        char s[2000];
        scanf("%s", s);
        string number(s);
        vector<int> n;
        bool find = true;
        int i = 0;
        while (find)
        {
            find = false;
            if (number.find('Z') != string::npos)
            {
                find = true;
                n.push_back(0);
                number.erase(number.find('Z'), 1);
                number.erase(number.find('E'), 1);
                number.erase(number.find('R'), 1);
                number.erase(number.find('O'), 1);
            }

            if (number.find('W') != string::npos)
            {
                find = true;
                n.push_back(2);
                number.erase(number.find('T'), 1);
                number.erase(number.find('W'), 1);
                number.erase(number.find('O'), 1);
            }

            if (number.find('U') != string::npos)
            {
                find = true;
                n.push_back(4);
                number.erase(number.find('F'), 1);
                number.erase(number.find('O'), 1);
                number.erase(number.find('U'), 1);
                number.erase(number.find('R'), 1);
            }

            if (number.find('X') != string::npos)
            {
                find = true;
                n.push_back(6);
                number.erase(number.find('S'), 1);
                number.erase(number.find('I'), 1);
                number.erase(number.find('X'), 1);
            }

            if (number.find('G') != string::npos)
            {
                find = true;
                n.push_back(8);
                number.erase(number.find('E'), 1);
                number.erase(number.find('I'), 1);
                number.erase(number.find('G'), 1);
                number.erase(number.find('H'), 1);
                number.erase(number.find('T'), 1);
            }
        }

        find = true;
        while (find)
        {
            find = false;
            if (number.find('O') != string::npos)
            {
                find = true;
                n.push_back(1);
                number.erase(number.find('O'), 1);
                number.erase(number.find('N'), 1);
                number.erase(number.find('E'), 1);
            }

            if (number.find_first_of("THR") != string::npos)
            {
                find = true;
                n.push_back(3);
                number.erase(number.find('T'), 1);
                number.erase(number.find('H'), 1);
                number.erase(number.find('R'), 1);
                number.erase(number.find('E'), 1);
                number.erase(number.find('E'), 1);
            }

            if (number.find('F') != string::npos)
            {
                find = true;
                n.push_back(5);
                number.erase(number.find('F'), 1);
                number.erase(number.find('I'), 1);
                number.erase(number.find('V'), 1);
                number.erase(number.find('E'), 1);
            }

            if (number.find('S') != string::npos)
            {
                find = true;
                n.push_back(7);
                number.erase(number.find('S'), 1);
                number.erase(number.find('E'), 1);
                number.erase(number.find('V'), 1);
                number.erase(number.find('E'), 1);
                number.erase(number.find('N'), 1);
            }
        }

        while (number.size()  > 0)
        {
            n.push_back(9);
            number.erase(number.find('N'), 1);
            number.erase(number.find('I'), 1);
            number.erase(number.find('N'), 1);
            number.erase(number.find('E'), 1);
        }

        string result = "";
        sort(n.begin(), n.end());
        for (int d : n)
        {
            result += to_string(d);
        }

        printf("Case #%d: %s\n", t, result.c_str());
    }
}