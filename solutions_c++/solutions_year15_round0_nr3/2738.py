#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <fstream>
#include <unordered_map>

using namespace std;

#include "Vector.h"


int main(int argc, const char **argv) {
    // close the iosnyc
    ios::sync_with_stdio(false);
    // file_path
    string file_path = "/Users/lxy/Downloads/";
    string file_name(argv[1]);
    file_path += file_name;
    // open the input file
    fstream file;
    file.open(file_path.c_str());
    /*
    if (file.is_open()) {
        cout<<"open successful!"<<endl;
    }
    else {
        cout<<"open failed!"<<endl;
    }
    */
    // number of the test cases
    int T;
    file >> T;
    vector<string> ret;
    // initial the multiply matrix
    unordered_map<char, int> umap;
    umap['1'] = 0;
    umap['i'] = 1;
    umap['j'] = 2;
    umap['k'] = 3;
    vector<vector<string> > multiply;
    vector<string> line1, line2, line3, line4;
    line1.push_back("1");
    line1.push_back("i");
    line1.push_back("j");
    line1.push_back("k");
    line2.push_back("i");
    line2.push_back("-1");
    line2.push_back("k");
    line2.push_back("-j");
    line3.push_back("j");
    line3.push_back("-k");
    line3.push_back("-1");
    line3.push_back("i");
    line4.push_back("k");
    line4.push_back("j");
    line4.push_back("-i");
    line4.push_back("-1");
    multiply.push_back(line1);
    multiply.push_back(line2);
    multiply.push_back(line3);
    multiply.push_back(line4);

    
    while (T > 0) {
        --T;
        // input the L and X
        long long L, X;
        file >> L;
        file >> X;
        // input the spells
        string tmp, spells;
        file >> tmp;
        for (int i = 1; i <= X; ++i) {
            spells += tmp;
        }
        // algorithm
        int sign = 0;
        string des = "ijk";
        int idx_des = 0;
        char pre = '1', prod;
        for (int idx = 0; idx < X * L; ++idx) {
            string tmp = multiply[umap[pre]][umap[spells[idx]]];
            if (tmp.size() == 2) {
                ++sign;
                prod = tmp[1];
            }
            else {
                prod = tmp[0];
            }
            pre = spells[idx] = prod;
            sign %= 2;
            if (spells[idx] == des[idx_des] && sign % 2 == 0) {
                if (idx_des != 2 || idx == X * L - 1) {
                    ++idx_des;
                    pre = '1';
                }
            }
        }

        // collect the results.
        if (idx_des == 3 && sign % 2 == 0) {
            ret.push_back("YES");
        }
        else {
            ret.push_back("NO");
        }
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
