#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
    ifstream ifile(argv[1]);
    int t = 0;
    ifile >> t;
    for (unsigned int i = 0; i < t; i++) {
        string tmp;
        ifile >> tmp;
        char lastchar = '+';
        int cnt = 0;
        for (int j = tmp.size() - 1; j >= 0; j--) {
            if (tmp[j] != lastchar) {
                cnt++;
                lastchar = tmp[j];
            }
        }
        cout << "Case #" << i + 1 << ": " << cnt << endl;
    }
    return 0;
}