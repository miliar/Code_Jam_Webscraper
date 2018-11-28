#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(int s_max, string levels) {
        int ans = 0, p_num = 0;
        for (int i = 0; i < levels.size(); ++i) {
            int tmp = i - p_num;
            if (levels[i] > 0 && tmp > 0) {
                ans += tmp;
                p_num += tmp;
            }
            p_num += levels[i] - '0';
        }
        return ans;
    }
};

int main() {
    int case_num, s_max, ans;
    string levels;
    Solution s;
    ifstream input("/Users/qianqianzhong/Documents/gcj2015/gcj/A-large.in");
    ofstream output("/Users/qianqianzhong/Documents/gcj2015/gcj/output.txt");
    input >> case_num;
    for (int i = 0; i < case_num; ++i) {
        input >> s_max >> levels;
        ans = s.solve(s_max, levels);
        output << "Case #" << i + 1 << ": " << ans;
        if (i != case_num - 1)
            output << endl;
    }
    input.close();
    output.close();
    return 0;
}
