#include <iostream>
#include <algorithm>
#include <vector>
#include <stdint.h>

using namespace::std;

void print(vector<int>& v)
{
    for (int i = 0; i < v.size(); ++i)
        cout << v[i];
    cout << endl;
}

int main ()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int N;
        cin >> N;

        int tmp = N;
        vector<int> v;
        while (tmp)
        {
            v.push_back(tmp % 10);
            tmp /= 10;
        }
        int key = 0;
        int64_t ans = -1;
        if (N > 0)
        for (int i = 1; i < 1000000; ++i)
        {
            int carry = 0;
            vector<int> u = v;
            for (int j = 0; j < u.size(); ++j)
            {
                int tmp = u[j] * i + carry;
                u[j] = tmp % 10;
                carry = tmp / 10;
            }

            while (carry)
            {
                u.push_back(carry % 10);
                carry = carry / 10;
            }

            //print(u);

            for (int j = 0; j < u.size(); ++j)
                key = key | (1 << u[j]);

            if (key == ((1 << 10) - 1))
            {
                ans = i * N;
//                cout << "key = " << key << endl;
                break;
            }
        }

        if (ans != -1) cout << "Case #" << t + 1 << ": " << ans << endl;
        else cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
    }
}
