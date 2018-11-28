#include <iostream>
#include <string>
#include <vector>

using namespace std;

string last_number(int num) {
    if (num == 0) { return "INSOMNIA"; }
    vector<bool> appear(10, false);
    int count = 10;
    int n = 0;
    while (count > 0) {
        n += num;
        for (int m = n; m > 0; m /= 10) {
            if (!appear[m % 10]) {
                --count;
                appear[m % 10] = true;
            }
        }
    }
    return to_string(n);
}

int main(int argc, char **argv) {
    for (int i = 2; i < argc; ++i) {
        cout << "Case #" << i - 1 << ": " << last_number(stoi(argv[i])) << endl;
    }
    return 0;
}