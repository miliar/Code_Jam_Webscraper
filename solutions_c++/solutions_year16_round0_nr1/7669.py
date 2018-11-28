#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool any(const vector<bool> &v)
{
    bool result = false;
    for (bool b : v)
        result = result || b;
    return result;
}

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        size_t N;
        cin >> N;

        if (N == 0)
        {
            cout << "Case #" << t << ": INSOMNIA\n";
            continue;
        }

        vector<bool> unseen(10, true);
        unsigned int i = 0;
        while (any(unseen))
        {
            size_t n = N * (++i);
            while (n)
            {
                unseen[n % 10] = false;
                n = (n - n%10)/10;
            }
        }
        cout << "Case #" << t << ": " << N*i << '\n';
    }
}
