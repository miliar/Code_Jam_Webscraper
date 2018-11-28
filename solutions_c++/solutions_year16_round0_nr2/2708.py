#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    string str;
    getline(cin, str);
    for (int i = 1; i <= T; i++) {
        getline(cin, str);
        int n = str.size();
        std::vector<int> D(n, 0);
        D[0] = str[0] == '+' ?0 :1;

        for (int j = 1; j < n; j++) {
            if(str[j] == '+') {
                D[j] = D[j-1];
                continue;
            }
            if (str[j-1] == '-') {
                D[j] = D[j-1];
            } else {
                D[j] = D[j-1] + 2;
            }
        }
        cout << "Case #" << i << ": " << D[n-1] << endl;
    }
    return 0;
}
