#include <fstream>
#include <cstdlib>
#include <cstring>

int standup(int up, char *str) {
    int len = strlen(str);
    for (int i = 0; i < len; ++i) {
        if (up >= i) {
            up += str[i] - '0';
            str[i] = '0';
        }
    }
    return up;
}

int main() {
    int t = 0;
    std::ifstream fin("test.in");
    std::ofstream fout("test.out");
    fin >> t;
    for (int i = 0; i < t; i++) {
        int s_max = 0, num_friend = 0;
        char *shyless;
        fin >> s_max;
        shyless = (char *)malloc((s_max + 1));
        fin >> shyless;
        // fout << s_max << " " << shyless;
        int goal = 0, up = 0;
        for (int j = 0; j <= s_max; ++j) {
            goal += shyless[j] - '0';
        }
        up = standup(up, shyless);
        while(up != goal) {
            ++num_friend;
            up += num_friend;
            up = standup(up, shyless);
            up -= num_friend;
        }
        fout << "Case #" << i + 1 << ": " << num_friend << std::endl;
    }
}
