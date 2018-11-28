#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int l;
        cin >> l;

        string s;
        cin >> s;

        int cur = 0, ret = 0;
        for (size_t j = 0; j < s.size(); ++j)
        {
            if (cur < j)
            {
                ret += (j - cur);
                cur = j;
            }

            cur += s[j] - '0';
        }

        cout << "Case #" << i + 1 << ": " << ret << endl;
    }

    return 0;
}
