#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    getchar();

    for (int testCase = 1; testCase <= T; ++testCase)
    {
        string S;
        getline(std::cin, S);

        string result;
        for (char c : S)
        {
            if (result.empty() || (result[0] > c))
            {
                result += c;
            }
            else
            {
                result = c + result;
            }
        }

        cout << "Case #" << testCase << ": " << result << endl;
    }

    return 0;
}
