#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <fstream>

using namespace std;

int main(void) {
    // close the iosnyc
    ios::sync_with_stdio(false);
    // open the input file
    string file_path = "/Users/lxy/Downloads/A-large.in";
    fstream file;
    file.open(file_path.c_str());
    // number of the test cases
    int T;
    file >> T;
    vector<int> ret;
    while (T > 0) {
        --T;
        // input the Smax and the string S
        int Sm;
        string S;
        file >> Sm;
        file >> S;
        // algorithm
        int need = 0, avail = S[0] - '0';
        if (S[0] == '0') {
            ++need;
            ++avail;
        }
        for (int idx = 1; idx <= Sm; ++idx) {
            if (avail < idx) {
                need += idx - avail;
                avail += idx - avail;
            }
            avail += S[idx] - '0';
        }

        // collect the result into a vector
        ret.push_back(need);
    }
    // test the result
    for (int idx = 0; idx < ret.size(); ++idx) {
        cout<<"Case #"<<idx + 1<<": "<<ret[idx];
        if (idx != ret.size() - 1) {
            cout<<endl;
        }
    }
    // close the file
    file.close();
    return 0;
}
