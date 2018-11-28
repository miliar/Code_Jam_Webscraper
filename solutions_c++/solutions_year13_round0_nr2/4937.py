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

using namespace std;

class CodeJame1 {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;
        for (int i = 0; i < case_number; ++i) {
            int N;
            int M;
            set<int> un_nums;
            input >> N;
            input >> M;
            vector<vector<int> > area;
            for (int n = 0; n < N; ++n) {
                vector<int> line;
                for (int m = 0; m < M; ++m) {
                    int num;
                    input >> num;
                    un_nums.insert(num);
                    line.push_back(num);
                }
                area.push_back(line);
            }
            WriteCaseResult(i+1, output, SolveProblem(area));
        }
        input.close();
        output.close();
    }
private:
    string DoCycleShift(const string& str, int num) {
        if (str.size() == 1)
            return str;
        return str.substr(num) + str.substr(0, num);
    }
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

    int MaxCol(const vector<vector<int> >& pattern, int col)
    {
        int max_v = -1;
        for (int r = 0; r < pattern.size(); ++r) {
            if (pattern[r][col] > max_v) {
                max_v = pattern[r][col];
            }
        }
        return max_v;
    }
    int MaxRow(const vector<vector<int> >& pattern, int row)
    {
        int max_v = -1;
        for (int c = 0; c < pattern[0].size(); ++c) {
            if (pattern[row][c] > max_v) {
                max_v = pattern[row][c];
            }
        }
        return max_v;
    }
    
    string SolveProblem(const vector<vector<int> >& pattern) {
        vector<vector<int> > area(pattern.size(), vector<int>(pattern[0].size(), 100));
        vector<vector<int> > max_row(pattern.size(), vector<int>(pattern[0].size(), 100));
        vector<vector<int> > max_col(pattern.size(), vector<int>(pattern[0].size(), 100));
        for (int r = 0; r < pattern.size(); ++r) {
            int max_v = MaxRow(pattern, r);
            
            for (int i =0; i < pattern[0].size(); ++i) {
                max_row[r][i] = max_v;
            }
        }
        for (int c = 0; c < pattern[0].size(); ++c) {
            int max_v = MaxCol(pattern, c);
            for (int i =0; i < pattern.size(); ++i) {
                max_col[i][c] = max_v;
            }
        }
        
        for (int i = 0; i < pattern.size(); ++i) {
            for (int j = 0; j < pattern[0].size(); ++j) {
                if (pattern[i][j] < max_row[i][j] && pattern[i][j] < max_col[i][j])
                    return "NO";
            }
        }
        return "YES";
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, string res) {
        output_stream << "Case #" << case_num << ": " << res << std::endl;
    }
};


int main() {
    CodeJame1  t;

    t.Solve("d:\\Sources\\CodeJam-2012\\input\\task1.txt", "d:\\Sources\\CodeJam-2012\\input\\task1_out.txt");

    return 0;
}