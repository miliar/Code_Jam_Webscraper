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
        int N;
        cin >> N;

        if (N == 0)
        {
            cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
            continue;
        }

        vector<bool> digits(10, false);

        int m = 1;
        int64_t result = N;
        while (true)
        {
            int64_t temp = result;
            while (temp != 0)
            {
                int digit = temp % 10;
                digits[digit] = true;
                temp /= 10;
            }

            bool all = true;
            for (int j = 0; j < 10; j++)
                if (!digits[j])
                {
                    all = false;
                    break;
                }

            if (all)
                break;

            result += N;
        }

        cout << "Case #" << (i + 1) << ": " << result << endl;
    }
}