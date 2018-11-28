#include <iostream>

using namespace std;

bool hashMap[10];

void record(int x) {
    string digits = to_string(x);
    for (auto digit: digits) {
        hashMap[digit - '0'] = true;
    }
}

int calculate(int x) {
    for (int i = 0; i < 10; ++i) {
        hashMap[i] = false;
    }

    record(x);
    int accumulate = x;
    while (!all_of(begin(hashMap), end(hashMap), [](bool h) { return h; })) {
        accumulate += x;
        record(accumulate);
    }

    return accumulate;
}

int main() {
    int t;
    int n;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> n;
        if (n != 0) {
            cout << "Case #" << i + 1 << ": " << calculate(n) << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        }
    }
    return 0;
}