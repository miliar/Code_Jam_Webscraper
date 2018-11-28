#include <iostream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

const char* ds[] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

// 0 = Z
// 6 = X
// 4 = U
// 2 = W
// 8 = G
// 5 = F - 4
// 7 = V - 5
// 1 = O - 0 - 2 - 4
// 3 = T - 2 -  8
// 9 = I - 5 - 6 - 8

int main() {
    int z;
    cin >> z;
    for (int cs=1; cs<=z; ++cs) {
        string s;
        cin >> s;
        vector<int> l(256);
        for (string::const_iterator it = s.begin(); it!=s.end(); ++it) {
            switch (*it) {
                case 'Z': case 'X': case 'U': case 'W': case 'G': case 'F': case 'V': case 'O': case 'T': case 'I':
                    l[int(*it)]++;
                    break;
            }
        }
        vector<int> d(10);
        d[0] = l['Z'];
        d[6] = l['X'];
        d[4] = l['U'];
        d[2] = l['W'];
        d[8] = l['G'];
        d[5] = l['F'] - d[4];
        d[7] = l['V'] - d[5];
        d[1] = l['O'] - d[0] - d[2] - d[4];
        d[3] = l['T'] - d[2] - d[8];
        d[9] = l['I'] - d[5] - d[6] - d[8];
        vector<int> num;
        for (int i=0; i<10; ++i) {
            for (int j=0; j<d[i]; ++j)
                num.push_back(i);
        }
        cout << "Case #" << cs << ": ";
        copy(num.begin(), num.end(), ostream_iterator<int>(cout, ""));
        cout << "\n";
    }
}
