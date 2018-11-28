#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

class CodeJame1 {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;
        for (int i = 0; i < case_number; ++i) {
            string s;
            int64 t;
            input >> s;
            input >> t;
            WriteCaseResult(i+1, output, SolveProblem(s, t));
        }
        input.close();
        output.close();
    }
private:
    string ToString(int64 value)
    {
        stringstream st;
        st << value;
        string res;
        st >> res;
        return res;
    }
    int64 ToNumber(const string& value)
    {
        stringstream st;
        st << value;
        int64 res;
        st >> res;
        return res;
    }

    bool is_c(char c) {
        return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
    }
    int Calc(string& s, int i, int len, int max_v) {
        int c = 0;
        for (int t = i; t < i + len; ++t) {
            if (!is_c(s[t])) {
                c = 0;
            } else {
                c++;
                if (c >= max_v)
                    return max_v;
            }
        }
        return -1;
    }
    
    int64 SolveProblem(string s, int64 t) {
        int64 res = 0;
        for (int i = 0; i < s.size(); ++i) {
            for (int len = 1; len <= s.size() - i; ++len) {
                if (Calc(s, i, len, t) == t) {
                    ++res;
                }
            }
        }
        return res;
    }

    void WriteCaseResult(int case_num, ofstream& output_stream, int64 res) {
        output_stream << "Case #" << case_num << ": " << res << std::endl;
    }
};


int main() {
    CodeJame1  t;

    t.Solve("d:\\Sources\\CodeJam-2012\\input\\task1.txt", "d:\\Sources\\CodeJam-2012\\input\\task1_out.txt");

    return 0;
}