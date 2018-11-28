#include <iostream>

using namespace std;

int main()
{
    int T, N;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N;

        if (N == 0)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else {
            int numberCount = 0;  // Store the info of the presence of numbers in binary form
            int nN = 0, n = 0;
            while (numberCount < 1024-1) {
                nN = (++n)*N;
                while (nN) {
                    numberCount = numberCount | (1 << nN%10);
                    nN = nN/10;
                }
            }
            cout << "Case #" << i << ": " << n*N << endl;
        }
    }
    return 0;
}
