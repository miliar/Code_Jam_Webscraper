#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        int smax;
        cin >> smax;
        string scnt;
        cin >> scnt;
        vector<int> s;
        for (string::const_iterator i = scnt.begin(); i != scnt.end(); ++i) {
            s.push_back(*i - '0');
        }
        int standed = 0;
        int extrareq = 0;
        for (int j = 0; j <= smax; ++j) {
            if (s[j] <= 0) continue;
            if (standed < j) {
                extrareq += j - standed;
                standed = j;
            }
            standed += s[j];
        }
        cout << extrareq << endl;
    }
    return 0;
}

