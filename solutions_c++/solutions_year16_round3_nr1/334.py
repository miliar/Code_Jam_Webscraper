#include <fstream>
#include <iostream>
#include <string>
#include <cmath>

#define BUFSIZE 1000

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int tests;
    char buf[BUFSIZE];

    int n;
    int p[26];
    int max1, max2;

    cin >> tests;
    cin.getline(buf, BUFSIZE);

    for (int t = 0; t < tests; t++) {

        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }

        //found max1
        max1 = 0;
        for (int i = 1; i < n; i++) {
            if (p[i] > p[max1]) max1 = i;
        }

        //found max2
        max2 = (max1 == 0) ? 1 : 0;
        for (int i = 1; i < n; i++) {
            if (p[i] > p[max2] && i != max1) max2 = i;
        }

        cout << "Case #" << t+1 << ": ";

        //equals two largest parties
        while (p[max1] > p[max2] + 1) {
            cout << (char)('A' + max1) << (char)('A' + max1) << " ";
            p[max1] -= 2;
        }
        if (p[max1] > p[max2]) {
            cout << (char)('A' + max1) << " ";
            p[max1]--;
        }

        //evacuate others
        for (int i = 0; i < n; i++) {
            if (i != max1 && i != max2) {
                while (p[i] > 1) {
                    cout << (char)('A' + i) << (char)('A' + i) << " ";
                    p[i] -= 2;
                }
                if (p[i] > 0) {
                    cout << (char)('A' + i) << " ";
                    p[i]--;
                }
            }
        }

        //evacuate last pairs
        while (p[max1] > 0) {
            cout << (char)('A' + max1) << (char)('A' + max2) << " ";
            p[max1]--;
            p[max2]--;
        }

        cout << endl;

    }

    cin.close();
    cout.close();

    return 0;
}
