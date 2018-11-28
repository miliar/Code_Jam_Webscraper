#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
using namespace std;

int main() {
    long long int t, n;
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    string s;
    fin >> t;
    for (long long int i = 1; i <= t; i++) {
        fin >> n >> s;
        long int sp = 0, ep = 0, c = 0;
        for (long long int k = 0; k <= n; k++) {
            if (s[k] == '0') {
                continue;
            }
            else if (k <= sp) {
                sp += (s[k]-48);
            }
            else {
                ep += k-sp;
                sp += (k-sp) + (s[k]-48);
            }
        }
        fout << "Case #" << i << ": " << ep << endl;
    }
    return 0;
}
