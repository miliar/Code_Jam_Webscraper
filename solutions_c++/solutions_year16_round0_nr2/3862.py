#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        std::string s;
        cin >> s;

        int result = 0;
        for (size_t i = 1; i < s.length(); ++i)
            if (s[i] != s[i - 1])
                ++result;
        
        if (s[s.length() - 1] == '-')
            ++result;

        cout << "Case #" << (i + 1) << ": " << result << '\n';
    }

    return 0;
}

