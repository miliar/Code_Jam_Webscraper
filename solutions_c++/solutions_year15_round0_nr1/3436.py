#include <iostream>
#include <cassert>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int run = 1; run <= T; ++run)
    {
        int Smax;
        string levels;
        cin >> Smax >> levels;

        assert((int)levels.size() == Smax + 1);

        int needed = 0;
        int standing = 0;
        for (int i = 0; i <= Smax; i++)
        {
            int count = levels[i] - '0';
            if (count && standing < i) {
                needed += i - standing;
                standing = i;
            }
            standing += count;
        }
        cout << "Case #" << run << ": " << needed << endl;
    }
}
