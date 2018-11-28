#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string a;
int op;

bool check() {
    for (int i = 0; i < a.length(); ++i) {
        if (a[i] == '-') {
            return false;
        }
    }
    return true;
}

ofstream fout("file2.txt");

int main() {
    int t;
    cin >> t;
    for (int foo = 1; foo <= t; ++foo) {
        op = 0;
        cin >> a;
        while (true) {
            if (check()) {
                break;
            }
            int i;
            for (i = 0; i < a.length() && a[i] == a[0]; ++i);
            for (int j = 0; j < i; ++j) {
                if (a[j] == '-') {
                    a[j] = '+';
                } else {
                    a[j] = '-';
                }
            }
            ++op;
        }
        cout << "Case #" << foo << ": ";
        fout << "Case #" << foo << ": ";
        cout << op << '\n';
        fout << op << '\n';
    }
    return 0;
}
