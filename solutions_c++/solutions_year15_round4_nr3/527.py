#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> dis;

int get(const string& s) {
    if(dis.count(s))
        return dis[s];
    else {
        int id = dis.size();
        return dis[s] = id;
    }
}

vector<int> s[20];

void read_line(vector<int>& v) {
    string ss;

    char c;
    while((c = getchar()) != '\n') {
        if(c == ' ') {
            v.push_back(get(ss));
            ss.clear();
        } else
            ss += c;
    }

    v.push_back(get(ss));
}

int m[2 * 1000 + 198 * 10];

int solve(int n, int k) {
    int mini = k;
    for(int mask = 0; mask < (1 << (n - 2)); mask++) {
        fill_n(m, k, 0);
        for(int i = 0; i < n; i++) {
            int flag = 1 << (i == 0 || (i != 1 && ((mask >> (i - 2)) & 1)));
            for(int ss : s[i])
                m[ss] |= flag;
        }
        mini = min(mini, (int) count(m, m + k, 3));
    }
    return mini;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        fprintf(stderr, "case %d...\n", i);

        dis.clear();

        int n;
        scanf("%d\n", &n);
        for(int j = 0; j < n; j++)
            read_line(s[j]);

        printf("Case #%d: %d\n", i, solve(n, dis.size()));

        for(int j = 0; j < n; j++)
            s[j].clear();
    }
}
