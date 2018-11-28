#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

void count(int n, int num_case) {
    vector<int> digits(10, 0);
    if (n == 0) {
        cout << "Case #" << num_case << ": INSOMNIA" << endl;
        return;
    }

    int cur = 0;
    for (int i = 1; cur != 10; ++i) {
        int data = n * i;
        while(data > 0) {
            int add = data % 10;
            if (digits[add] == 0) {
                cur++;
                digits[add] = 1;
            }
            data /= 10;
        }
        if (cur == 10) {
            cout << "Case #" << num_case << ": " << n * i << endl;
        }
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("sol1.out", "w", stdout);

    int t, n;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> n;
        count(n, i + 1);
    }
    fclose(stdin);
    return 0;
}