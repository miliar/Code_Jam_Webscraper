#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

vector <string> given, conf;

bool valid(vector <string> &conf) {
    string concat = "";
    for (int i = 0; i < conf.size(); ++i) {
        concat += conf[i];
    }





    for (int i = 0; i < concat.size(); ++i) {
        int c = concat[i] - 'a';
        if (last_occ[c] == -1 || last_occ[c] == i - 1) {
            last_occ[c] = i;
            continue;
        }

        return false;

    }

    return true;
}

int answer = 0;
int last_occ[26];

void solve(int pos, int mask) {
    if (pos == given.size()) {
        if (valid(conf)) {
            answer++;
        }
        return;
    }
    for (int i = 0; i < given.size(); ++i) {
        if (mask & (1<<i)) continue;
        conf[pos] = given[i];
        solve(pos + 1, mask | (1<<i));
    }
}

int main() {
    int tests, n;
    scanf("%d", &tests);
    for (int case_no = 1; case_no <= tests; ++case_no) {
        scanf("%d", &n);
        char str[128];
        given.clear();
        for (int i = 0; i < n; ++i) {
            scanf("%s", str);
            given.push_back(str);
        }

        for (int i = 0; i < 26; ++i) {
                last_occ[i] = -1;
        }

        answer = 0;
        conf = given;
        solve(0, 0);
        printf("Case #%d: %d\n", case_no, answer % 1000000007);
    }

}
