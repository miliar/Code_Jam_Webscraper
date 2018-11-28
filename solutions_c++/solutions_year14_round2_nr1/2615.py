#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases+1; ++c)
    {
        int N;
        is >> N;

        vector<string> s(N);
        for (int i(0); i < N; ++i) is >> s[i];

        vector<string> unique(N);
        for (int i(0); i < N; ++i) {
            unique[i].push_back(s[i][0]);
            for (int j(1); j < s[i].size(); ++j)
                if (unique[i][unique[i].size()-1] != s[i][j]) unique[i].push_back(s[i][j]);
        }

        bool possible(true);
        for (int i(1); i < N; ++i) {
            if (unique[i] != unique[i-1]) {
                cout << "Case #" << c << ": Fegla Won" << endl;
                possible = false;
                break; 
            }
        }
        if (!possible) continue;

        int uni_len = unique[0].size();
        int length[N][uni_len];
        for (int i(0); i < N; ++i) {
            for (int k(0); k < uni_len; ++k) length[i][k] = 0;
            int k(0);
            for (int j(0); j < s[i].size(); ++j) {
                if (unique[i][k] == s[i][j]) ++length[i][k];
                else { ++k; ++length[i][k]; }
            }
        }

        int nb(0);
        for (int k(0); k < uni_len; ++k) {
            int sum(0);
            for (int i(0); i < N; ++i) {
                sum += length[i][k];
            }
            double mean = static_cast<double>(sum)/N;
            //cout << "mean = " << mean << endl;
            for (int i(0); i < N; ++i) {
                nb += abs(static_cast<int>(mean) - length[i][k]);
            }
        }

        cout << "Case #" << c << ": " << nb << endl;
    }
}

