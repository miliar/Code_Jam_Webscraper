#include <iostream>
#include <string>
using namespace std;

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string str;
        cin >> str;
        int n = str.size();
        string ret;
        for (int j = 0; j < n; j++) {
            if (j == 0) {
                ret.push_back(str[j]);
            } else {
                if (str[j] >= ret[0]) {
                    ret = str[j] + ret;
                } else {
                    ret = ret + str[j];
                }
            }
        }
        cout << "Case #" << i << ": " << ret << endl;
        getline(cin, str);
    }
    return 0;
}
