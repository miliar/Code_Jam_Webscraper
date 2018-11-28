#include <iostream>
#include <algorithm>

bool isSameChar(const std::string& s)
{
    return s.empty() || s.find_first_not_of(s[0]) == std::string::npos;
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        std::string S;
        std::cin >> S;
        int flips = 0;
        char prevSign = S[0];
        if (!isSameChar(S))
        {
            for (int i = 1; i < S.length(); ++i)
            {
                if (prevSign != S[i]) flips++;
                prevSign = S[i];
            }
        }
        if (S[S.length()-1] == '-') flips++;
        std::cout << "Case #" << i << ": " << flips << std::endl;
    }
}
