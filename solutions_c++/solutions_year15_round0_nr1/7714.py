#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream ifs("/Users/zhengxx/Projects/cplusplus/Algorithms/Codejam/input/A-large.in");
    ofstream ofs("/Users/zhengxx/Projects/cplusplus/Algorithms/Codejam/input/output_large.txt");
    int n;
    ifs >> n;

    int c = 0;
    while (c++ < n) {
        int s_max;
        string str;
        ifs >> s_max >> str;
        int sum = 0, need = 0;
        for (int i = 0; i < str.size(); i++) {
            int temp = i - sum;
            need = max(need, max(0, temp));
            sum += str[i] - '0';
        }
        ofs << "Case #" << c << ": " << need << endl;
    }

    return 0;
}