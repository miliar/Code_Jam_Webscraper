#include <iostream>
#include <string>
#include <deque>
#include <cstring>

typedef unsigned int uint;
typedef unsigned long long uint64;

using namespace std;

int main()
{
    uint num_entries = 0;
    cin >> num_entries;

    for (int i = 0; i < num_entries; i++)
    {
        string s;
        cin >> s;

        const char *sp = s.c_str();

        deque<char> str;

        for (int j = 0; j < strlen(s.c_str()); j++)
        {
            if (str.size() == 0)
            {
                str.push_back(sp[j]);
            }
            else
            {
                if (sp[j] >= str.front())
                {
                    str.push_front(sp[j]);
                }
                else
                {
                    str.push_back(sp[j]);
                }
            }
        }

        cout << "Case #" << i + 1 << ": ";

        for (auto k : str)
        {
            cout << k;
        }

        cout << endl;
    }
    return 0;
}