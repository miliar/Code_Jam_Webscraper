#include <iostream>

using namespace std;

void so(int num) {
    int s, i, total, fr;
    cin >>s;
    char p;
    total = 0;
    fr = 0;
    for (i = 0; i <= s; i++) {
        cin >>p;
        while (p<'0' || p>'9') {
            cin >>p;
        }
        if (total < i) {
            fr += i - total;
            total = i;
        }
        total += p - '0';
    }
    cout << "Case #" << num+1 <<": " << fr <<endl;
}

int main() {
    int t, i;
    cin >>t;
    for (i = 0; i < t; i++) {
        so(i);
    }
    exit(0);
}