#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("test.in");
    ofstream cout("test.out");

    int t;
    cin >> t;
    for (int k = 0; k < t; k++) {
        int n;
        cin >> n;

        char ch;
        long long all = 0;
        long long fake = 0;

        for (int i = 0; i <= n; i++) {
            cin >> ch;
            int kil = ch-48;

            if (all < i) {
                fake += (i-all);
                all += (i-all);
            }
            all += kil;
        }
        cout << "Case #" << k+1 << ": " << fake << endl;
    }

}
