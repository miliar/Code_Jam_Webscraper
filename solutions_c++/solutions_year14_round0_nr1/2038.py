#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

void skip_row()
{
    int t;
    cin >> t >> t >> t >> t;
}

string solve()
{
    vector<int> nums(16, 0);

    int r;

    for (int k = 0; k < 2; ++k)
    {
        cin >> r;
        for (int i = 1; i <= 4; ++i) 
            for (int j = 1; j <= 4; ++j)
            {
                int t;
                cin >> t;

                if (r == i) ++nums[t - 1];
            }
    }

    int c = count(nums.begin(), nums.end(), 2);
    if (!c) return "Volunteer cheated!";
    if (c > 1) return "Bad magician!";

    ostringstream str;
    str << find(nums.begin(), nums.end(), 2) - nums.begin() + 1;
    return str.str();
}

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
}

