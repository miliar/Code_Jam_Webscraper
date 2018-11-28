// g++ -Wall sample.cc
// ./a.out <sample-input.txt >output.txt

#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <string.h>
#include <queue>
using namespace std;
typedef pair<int, int> P;
typedef long long ll;
const int MAX_N = 105;
int T;
int N;
int current_i[MAX_N];
int main(int argc, const char * argv[])
{
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d", &N);
        vector<string> strings;
        for (int i = 0; i < N; i++) {
            string s;
            cin >> s;
            strings.push_back(s);
        }
        set<string> short_strings;
        for (int i = 0; i < N; i++) {
            string s = strings[i];
            string sh = "";
            int index = 0;
            while (index < s.size()) {
                sh += s[index];
                int di = 1;
                while (index + di < s.size() && s[index] == s[index + di]) {
                    di++;
                }
                index += di;
            }
            short_strings.insert(sh);
        }
        if (short_strings.size() != 1) {
            printf("Case #%d: Fegla Won\n", t+1);
        } else {
            int ret = 0;
            set<string>::iterator it = short_strings.begin();
            string sh = *it;
            memset(current_i, 0, sizeof(current_i));
            for (int i = 0; i < sh.size(); i++) {
                char c = sh[i];
                vector<int> num;
                double all = 0;
                for (int j = 0; j < N; j++) {  //cの数を数える
                    int index = current_i[j];
                    int di = 0;
                    while (index+di < strings[j].size() && strings[j][index+di] == c) {
                        di++;
                    }
                    current_i[j] = index + di;
                    num.push_back(di);
                    all += di;
                }
                int base = (int)(all/N + 0.5);  //四捨五入
                for (int j = 0; j < N; j++) {
                    ret += abs(base - num[j]);
                }
            }
            printf("Case #%d: %d\n", t+1, ret);
        }
    }
    return 0;
}

