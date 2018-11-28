#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int pts(const vector<double>& p1, const vector<double>& p2)
{
    int n = p1.size();

    auto i1 = p1.rbegin();
    auto i2 = p2.rbegin();

    int result = 0;
    while (i1 != p1.rend() && i2 != p2.rend())
    {
        if (*i1 > *i2)
        {
            ++result;
            ++i1;
            ++i2;
        }
        else
        {
            ++i2;
        }
    }
    return result;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n;
        cin >> n;
        vector<double> naomi(n);
        vector<double> ken(n);

        for (int j = 0; j < n; ++j)
            cin >> naomi[j];
        for (int j = 0; j < n; ++j)
            cin >> ken[j];
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        cout << "Case #" << i + 1 << ": " << pts(naomi, ken) << ' ' << n - pts(ken, naomi) << endl;
    }
    return 0;
}
