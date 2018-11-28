#include <iostream>
using namespace std;

string s;

void go() {
    int n;
    cin >> n >> s;
    n++;
    int c = 0;
    long long a = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] > '0' && c + a < i) {
            a += i - c - a;
        }
        c += s[i] - '0';
    }
    cout << a;
}

int main() {
    int tn;
    cin >> tn;
    for (int i = 0; i < tn; i++) {
        cout << "Case #" << i + 1 << ": ";
        go();
        cout << endl;
    }
}