#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    for (int b = 0; b < tc; ++b) {
        int inp[1005], req = 0, standing = 0, num;
        char people;
        cin >> num;
        for (int a = 0; a <= num; ++a) {
            cin >> people;
            inp[a] = people - '0';
        }
        for (int a = 0; a <= num; ++a) {
            if (standing >= a) standing += inp[a];
            else {
                req += (a - standing);
                standing = a + inp[a];
            }
        }
        cout << "Case #" << b + 1 << ": " << req << "\n";
    }
    return 0;
}