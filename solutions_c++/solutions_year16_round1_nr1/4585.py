#include <iostream>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[]) {
    int t;
    char lw[300];
    string s;
    cin >> t;
    getline(cin, s);
    for (int i = 0; i < t; i++) {
        int start, end;
        start = end = 150;
        const char *ps = s.c_str();
        getline(cin, s);
        lw[start] = ps[0];
        for (int j = 1; j < s.size(); j++) {
            if (lw[start] > ps[j]) {
                lw[++end] = ps[j];
            } else {
                lw[--start] = ps[j];
            }
        }
        lw[++end] = '\0';
        cout << "Case #" << i + 1 << ": " << lw + start << endl;
    }

    return 0;
}
