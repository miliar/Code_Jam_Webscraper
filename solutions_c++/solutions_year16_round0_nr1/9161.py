#include <iostream>

using namespace std;


long long check(const int n) {
    long long int num = 0;

    bool seen[10] = { false };
    while (true) {
        num += n;
        long long v = num;
        while (v != 0) {
            seen[ v % 10 ] = true;
            v /= 10;
        }

        bool anyFalse = false;
        for (int i = 0; i < 10; ++i) {
            if (!seen[i]) {
                anyFalse = true;
                break ;
            }
        }
        if (!anyFalse) {
            break ;
        }
    }
    return num;
}


int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int n;
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << check(n) << endl;
        }
    }
    return 0;
}
