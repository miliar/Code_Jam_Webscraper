#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <climits>

using namespace std;

int main()
{
    string line;
    int T;
    getline(cin, line); stringstream ssT(line); ssT >> T;
    for (int testcase = 0; testcase < T; testcase++) {
        cout << "Case #" << testcase+1 << ": ";

        int N;
        getline(cin, line); stringstream ssN(line); ssN >> N;
        unordered_map<string, uint32_t> dict;
        for (int i = 0; i < N; i++) {
            getline(cin, line); stringstream ssW(line);
            while (ssW) {
                string word;
                ssW >> word;
                if (word.size() > 0) {
                    dict[word] = dict[word] | (1 << i);
                }
            }
        }

        int min = INT_MAX;
        uint32_t M = 1 << N;
        for (uint32_t i = 0; i < M; i += 4) {
            int count = 0;
            uint32_t MM = i + 2;
            for (auto w = dict.begin(); w != dict.end(); w++)
                if ((w->second & MM) != 0 && (w->second & ~MM) != 0)
                    count++;
            if (count < min)
                min = count;
        }

        cout << min << endl;
    }
    return 0;
}

// vim: set sw=4:
