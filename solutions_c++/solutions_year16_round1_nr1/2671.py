#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int t_i = 0; t_i < n; t_i++)
    {
        string s;
        cin >> s;

        string result;

        for (auto c : s)
        {
            if (result.size() == 0)
                result += c;
            else
            {
                if (c >= result[0])
                    result = string(1, c) + result;
                else
                    result += c;
            }
        }

        cout << "Case #" << t_i + 1 << ": ";

        cout << result;

        cout << endl;
    }
}
