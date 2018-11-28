#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(const vector<int> &mas)
{
    int ans = 10004;
    int max_element = *std::max_element(mas.begin(), mas.end());

    for (int time = 1; time <= max_element; ++time)
    {
        int spesial_minutes = 0;
        for (int i = 0; i < mas.size(); ++i)
        {
            spesial_minutes += mas[i] / time;
            if (mas[i] % time == 0)
            {
                --spesial_minutes;
            }
        }

        ans = min(ans, time + spesial_minutes);
    }

    return ans;
}

int main(int argc, char* argv[])
{
    ios_base::sync_with_stdio(false);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int test = 0; test < T; ++test)
    {
        int d;
        cin >> d;

        vector<int> mas(d);
        for (int & x : mas)
        {
            cin >> x;
        }

        cout << "Case #" << test + 1 << ": " << solve(mas) << "\n";
    }

    return 0;
}

