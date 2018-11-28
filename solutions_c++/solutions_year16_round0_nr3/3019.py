#include <iostream>
using namespace std;

long long int factor(long long int n)
{
    for (long long i = 2; i <= n / i; i++)
        if (n % i == 0)
            return i;
    return 0;
}

long long int convertbase(long long int n, int b)
{
    long long int ret = 0, temp = 1;
    while (n) {
        //ret += (n % 2) * temp;
        //n /= 2;
        //temp *= b;
        // Reversing give results much faster reults
        ret *= b;
        ret += (n % 2);
        n /= 2;

    }
    return ret;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, J, sols = 0;
        cin >> N >> J;
        cout << "Case #" << t + 1 << ": " << endl;
        for (long long int i = (1 << (N - 1)) + 1; i <= (1 << (N)) - 1;
             i += 2) {
            bool fit = true;
            for (int j = 2; j <= 10; j++)
                if (!factor(convertbase(i, j))) {
                    fit = false;
                    break;
                }
            if (fit) {
                sols++;
                cout << convertbase(i, 10) << " ";
                for (int j = 2; j <= 10; j++)
                    cout << factor(convertbase(i, j)) << " ";
                cout << endl;
                if (sols >= J)
                    break;

            }
        }
    }
    return 0;
}
