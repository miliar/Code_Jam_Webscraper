#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
    int T;
    cin >> T;
    unsigned long long N;
    for (int cas = 1; cas <= T; ++cas)
    {
        cout << "Case #" << cas << ": ";
        bitset<10> all_10;
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        auto lastN = 0ULL;
        do {
#ifdef DEBUG
            cout << lastN << " ";
#endif
            lastN += N;
            for (auto ncopy = lastN; ncopy;) {
                // get last digit
                int digit = ncopy % 10;
                all_10.set(digit);
                ncopy /= 10;
            }
        }while (!all_10.all()) ;
        cout << lastN << "\n";
    }

    return 0;
}
