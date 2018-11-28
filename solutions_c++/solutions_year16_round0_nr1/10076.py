#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void test_case(int counter) {
    int n;
    cin >> n;
    if (n == 0) {
        cout << "Case #" << counter << ": INSOMNIA" << endl;
        return;
    }
    int d[10] = {0};
    int found = 0;
    int mult = 0;

    while (found != 10) {
        ++mult;
        int N = n * mult;
        string str = to_string(N);
        for (int i = 0; i < str.size(); ++i) {
            int idx = str[i] - '0';
            ++d[idx];
            if (d[idx] == 1) ++found;
        }
    }
    cout << "Case #" << counter << ": " << mult * n << endl;
}

int main() {
    int cases;
    cin >> cases;
    int counter = 1;
    while (cases--) test_case(counter++);
}
