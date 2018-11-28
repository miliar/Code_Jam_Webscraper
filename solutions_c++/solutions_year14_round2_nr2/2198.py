#include <iostream>

using namespace std;

int main()
{
    int T;
    long long A, B, K;
    long long a, b;
    long long result;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases)
    {
        cin >> A >> B >> K;
        result = 0;
        for (a = 0; a < A; ++a)
            for (b = 0; b < B; ++b)
                if ((a&b) < K)
                {
                    //cout << a << ", " << b << endl;
                    ++result;
                }
        cout << "Case #" << cases << ": " << result << endl;
    }
    return 0;
}
