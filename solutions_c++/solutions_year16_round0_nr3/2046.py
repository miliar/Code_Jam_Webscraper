#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ifstream inf("input.txt");
    ofstream outf("output.txt");

    int t; inf >> t;
    int n; inf >> n;
    int j; inf >> j;
    outf << "Case #1:\n";

    vector<int> num(n, 0);
    num[0] = 1; num[n - 1] = 1;
    int divs[9];
    int cnt = 0;
    while (cnt < j) {
        /*for (int i = 0; i < n; i++) {
            cout << num[i];
        }
        cout << endl;*/
        bool is_p = false;
        for (int b = 2; b <= 10; b++) {
            /*unsigned int m = 0;
            for (int i = 0; i < n; i++) {
                m = m * b + num[i];
            }*/
            int u = 0;
            double v = 0;
            double p = 1;
            for (int i = n - 1; i >= 0; i--) {
                v += num[i]*p;
                p *= sqrt(b);
            }
            u = v;
            //cout << v << endl;
            divs[b - 2] = -1;
            for (int i = 2; i <= min(v, 100000.0); i++) {
                int o = 0;
                int o1 = 1;
                for (int k = n - 1; k >= 0; k--) {
                    o = (o + (num[k]*o1)) % i;
                    o1 = (o1*b) % i;
                }
                if (o == 0) {
                    divs[b - 2] = i;
                    break;
                }
            }
            if (divs[b - 2] == -1) {
                is_p = true;
                break;
            }
        }
        if (!is_p) {
            for (int i = 0; i < n; i++) {
                outf << num[i];
            }
            for (int i = 0; i < 9; i++) {
                outf << ' ' << divs[i];
            }
            ++cnt;
            cout << cnt << endl;
            outf << '\n';
        }
        int i = n - 2;
        while (num[i] == 1 && i > 0) {
            num[i] = 0;
            --i;
        }
        if (i == 0) {
            break;
        }
        num[i] = 1;
    }
}