#include <iostream>
#include <set>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        cout << "Case #" << (t + 1) << ": ";
        int N;
        cin >> N;

        if (N == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }

        set<int> digits;
        int KN = 0;
        while (digits.size() != 10)
        {
            KN += N;
            int tmp = KN;
            while (tmp > 0)
            {
                digits.insert(tmp % 10);
                tmp /= 10;
            }
        }

        cout << KN << endl;
    }

    return 0;
}
