#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        string s;
        cin >> s;
        int result = 0;

        while (true)
        {
            bool blank = false;
            int flipIndex = -1;
            for (int j = 0; j < s.length(); j++)
            {
                if (s[j] == '-')
                    blank = true;
                else if (blank /*&& s[j] == '+'*/)
                {
                    flipIndex = j;
                    blank = false;
                    break;
                }
            }

            if (blank && flipIndex == -1)
                flipIndex = s.length();

            if (flipIndex == -1)
                break;

            for (int j = 0; j < flipIndex; j++)
            {
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
            result++;
        }

        cout << "Case #" << (i + 1) << ": " << result << endl;
    }
}