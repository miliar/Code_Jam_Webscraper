#include <iostream>
#include <fstream>
#include <string>
using namespace std;

///ifstream fin("b.in");
///ofstream fout("b.out");

string a;
int op;
int T, pos;

bool check() {
    int Size = a.length();
    for (int i = 0; i < Size; ++i) {
        if (a[i] == '-') {
            return false;
        }
    }
    return true;
}

int main() {
    cin >> T;
    while(T--) {
        ++pos;
        op = 0;
        cin >> a;
        while (true) {
            if (check()) {
                break;
            }
            int i;
            int Size = a.length();
            for (i = 0; i < Size && a[i] == a[0]; ++i);
            for (int j = 0; j < i; ++j) {
                if (a[j] == '-') {
                    a[j] = '+';
                }
                else {
                    a[j] = '-';
                }
            }
            ++op;
        }
        cout << "Case #" << pos << ": ";
        cout << op << '\n';
    }
    return 0;
}
