#include <fstream>
#include <string>
#include <deque>
#include <vector>
#include <map>
#include <array>
#include <algorithm>

std::ifstream in("in.txt");
std::ofstream out("out.txt");


int main()
{
    int T;
    in >> T;
    for (int t = 0; t < T; ++t) {
        std::string s;
        in >> s;
        std::vector<int> cnt(300, 0);
        std::vector<int> digs;
        for (size_t i = 0; i < s.size(); ++i)
            cnt[s[i]]++;
        if (cnt['Z'] > 0) {
            for (int j = 0; j < cnt['Z']; ++j)
                digs.push_back(0);
            cnt['E'] -= cnt['Z'];
            cnt['R'] -= cnt['Z'];
            cnt['O'] -= cnt['Z'];
            cnt['Z'] = 0;
        }
        if (cnt['X'] > 0) {
            for (int j = 0; j < cnt['X']; ++j)
                digs.push_back(6);
            cnt['S'] -= cnt['X'];
            cnt['I'] -= cnt['X'];
            cnt['X'] = 0;
        }
        if (cnt['S'] > 0) {
            for (int j = 0; j < cnt['S']; ++j)
                digs.push_back(7);
            cnt['E'] -= 2 * cnt['S'];
            cnt['V'] -= cnt['S'];
            cnt['N'] -= cnt['S'];
            cnt['S'] = 0;
        }
        if (cnt['V'] > 0) {
            for (int j = 0; j < cnt['V']; ++j)
                digs.push_back(5);
            cnt['I'] -= cnt['V'];
            cnt['F'] -= cnt['V'];
            cnt['E'] -= cnt['V'];
            cnt['V'] = 0;
        }
        if (cnt['U'] > 0) {
            for (int j = 0; j < cnt['U']; ++j)
                digs.push_back(4);
            cnt['F'] -= cnt['U'];
            cnt['O'] -= cnt['U'];
            cnt['R'] -= cnt['U'];
            cnt['U'] = 0;
        }
        if (cnt['W'] > 0) {
            for (int j = 0; j < cnt['W']; ++j)
                digs.push_back(2);
            cnt['T'] -= cnt['W'];
            cnt['O'] -= cnt['W'];
            cnt['W'] = 0;
        }
        if (cnt['O'] > 0) {
            for (int j = 0; j < cnt['O']; ++j)
                digs.push_back(1);
            cnt['N'] -= cnt['O'];
            cnt['E'] -= cnt['O'];
            cnt['O'] = 0;
        }
        if (cnt['R'] > 0) {
            for (int j = 0; j < cnt['R']; ++j)
                digs.push_back(3);
            cnt['E'] -= 2 * cnt['R'];
            cnt['T'] -= cnt['R'];
            cnt['H'] -= cnt['R'];
            cnt['R'] = 0;
        }
        if (cnt['N'] > 0) {
            for (int j = 0; j < cnt['N'] / 2; ++j)
                digs.push_back(9);
            cnt['E'] -= cnt['N'] / 2;
            cnt['I'] -= cnt['N'] / 2;
            cnt['N'] = 0;
        }
        for (int j = 0; j < cnt['E']; ++j)
            digs.push_back(8);
        out << "Case #" << t + 1 << ": ";
        std::sort(digs.begin(), digs.end());
        for (size_t j = 0; j < digs.size(); ++j)
            out << digs[j];
        out << std::endl;
    }
    return 0;
}
