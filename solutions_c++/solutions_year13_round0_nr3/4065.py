#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool isPalindrom(long long a)
{
    ostringstream oss;
    oss << a;
    string z = oss.str();
    for (int i = 0; i < z.size() / 2; ++i)
        if (z[i] != z[z.size() - i - 1]) return false;
    return true;
}

int main()
{
    int T;
    cin >> T;
    vector<long long> z;
    for (long long i = 1; i <= 10000000; ++i)
    {
        if (isPalindrom(i) && isPalindrom(i * i))
        {
            z.push_back(i);
        }
    }
    for (int t = 1; t <= T; ++t)
    {
        long long ans = 0;
        long long A, B;
        cin >> A >> B;
        for (int i = 0; i < z.size(); ++i)
        {
            if ((z[i] * z[i] >= A) && (z[i] * z[i] <= B))
                ++ans;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}