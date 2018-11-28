#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int singlecase(int N) {
    if (N < 1)
        return 0;
    int R = N;
    int cnt = 10;
    int map[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
    while (true) {
        stringstream ss;
        ss << R;
        for (char ch: ss.str()) {
            cnt -= map[ch - '0'];
            map[ch - '0'] = 0;
        }
        if (cnt == 0)
            break;
        R += N;
    };
    return R;
}

int main() {
    string s;
    int numCases = 0;
    getline(cin, s);
    stringstream(s) >> numCases;

    for (int i = 1; i <= numCases; ++i) {
        // read N
        int N = -1;
        getline(cin, s);
        stringstream(s) >> N;
        N = singlecase(N);
        cout << "Case #" << i << ": ";
        if (N > 0)
            cout << N << endl;
        else
            cout << "INSOMNIA" << endl;
    }

}

