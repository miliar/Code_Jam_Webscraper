#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    int T;
    int Smax;
    char c;
    int n;
    int f;

    cin >> skipws;
    cin >> T;

    for(int t = 0; t < T; t++) {
        cin >> Smax;
        n = 0;
        f = 0;

        for(int i = 0; i <= Smax; i++) {
            if(n < i) {
                f += i - n;
                n = i;
            }

            cin >> c;
            n += c - '0';
        }

        cout << "Case #" << t + 1 << ": " << f << endl;
    }

    return 0;
}
