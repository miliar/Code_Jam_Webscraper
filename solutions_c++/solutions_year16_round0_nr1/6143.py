#include <iostream>
#include <fstream>
using namespace std;

int n;
int fr[10];

void count(int n) {
    while (n) {
        ++fr[n % 10];
        n /= 10;
    }
}

bool check() {
    for (int i = 0; i < 10; ++i) {
        if (fr[i] == 0) {
            return false;
        }
    }
    return true;
}

void clear() {
    for (int i = 0; i < 10; ++i) {
        fr[i] = 0;
    }
}

ofstream fout("file.txt");

int main() {
    int t;
    cin >> t;
    for (int foo = 1; foo <= t; ++foo) {
        cin >> n;
        cout << "Case #" << foo << ": ";
        fout << "Case #" << foo << ": ";
        if (n == 0) {
            cout << "INSOMNIA\n";
            fout << "INSOMNIA\n";
        } else {
            for (int i = 1; ; ++i) {
                count(n * i);
                if (check()) {
                    cout << n * i << '\n';
                    fout << n * i << '\n';
                    break;
                }
            }
        }
        clear();
    }
}
