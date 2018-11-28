#include <iostream>
#include <bitset>
#include <string>
#include <algorithm>

void flip(std::string& s, int pos) // [0, pos[
{
    for (int i = 0; i <= pos; i++)
    {
        s[i] = (s[i] == '+' ? '-' : '+');
    }
}

int main()
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        std::string S;
        std::cin >> S;

        int count = 0;

        while (!std::all_of(S.begin(), S.end(), [](char c) { return c == '+'; }))
        {
            int i;
            for (i = S.size() - 1; i >= 0 && S[i] != '-'; --i)
            {             
            }

            flip(S, i);
            count++;
        }

        std::cout << "Case #" << t + 1 << ": " << count << "\n";
    }
}
