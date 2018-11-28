#include <iostream>
#include <string>
#include <map>
#include <vector>

int abs(int x) {
    return (x > 0) ? x : -x;
}

int cost(std::vector<std::vector<std::pair<char, unsigned>>>& v) {
    unsigned N = v.size();
    int diff = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (v[i].size() != v[j].size()) return -1;
            for (int k = 0; k < v[i].size(); k++) {
                if (v[i][k].first != v[j][k].first) return -1;
            }
        }
    }
    for (int i = 0; i < v[0].size(); i++) {
        unsigned sum = 0;
        for (int j = 0; j < N; j++) {
            sum += v[j][i].second;
        }
        unsigned mean = sum / N;
        for (int j = 0; j < N; j++) {
            diff += abs(v[j][i].second - mean);
        }
    }
    return diff;
}

int main()
{
    int T; std::cin >> T; std::cin.ignore();

    for (int i = 1; i <= T; ++i) {
        int N; std::cin >> N; std::cin.ignore();

        std::vector<std::vector<std::pair<char, unsigned>>> v;
        v.reserve(N);

        for (int j = 0; j < N; ++j) {
            std::string s;
            std::getline(std::cin, s);
            v.push_back(std::vector<std::pair<char,unsigned>>(1, std::make_pair(s[0], 1)));
            for (int k = 0; k < s.size(); ++k) {
                if (s[k] != v[j].back().first) {
                    v[j].push_back(std::make_pair(s[k], 1));
                } else {
                    v[j].back().second++;
                }
            }

        }

        int diff = cost(v);

        if (diff >= 0) {
            std::cout << "Case #" << i << ": " << diff << std::endl;
        } else {
            std::cout << "Case #" << i << ": Fegla Won" << std::endl;
        }
    }
}
