#include <cstdio>
#include <vector>
#include <string>

using namespace std;

struct rps {
    int r;
    int p;
    int s;
    string line;
};

vector <rps> v[13];

int main() {
    int t, i, j, k;
    
    v[0].push_back((rps){1, 0, 0, "R"});
    v[0].push_back((rps){0, 1, 0, "P"});
    v[0].push_back((rps){0, 0, 1, "S"});
    
    for (i = 1; i <= 12; i++) {
        for (j = 0; j < 3; j++) {
            v[i].push_back((rps){v[i - 1][j].r + v[i - 1][(j + 2) % 3].r, v[i - 1][j].p + v[i - 1][(j + 2) % 3].p, v[i - 1][j].s + v[i - 1][(j + 2) % 3].s, min(v[i - 1][j].line + v[i - 1][(j + 2) % 3].line, v[i - 1][(j + 2) % 3].line + v[i - 1][j].line)});
        }
    }
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, r, p, s;
        
        scanf("%d %d %d %d", &n, &r, &p, &s);
        
        printf("Case #%d: ", i + 1);
        
        for (j = 0; j < v[n].size(); j++) {
            if (v[n][j].r == r && v[n][j].p == p && v[n][j].s == s) {
                printf("%s\n", v[n][j].line.c_str());
                break;
            }
        }
        
        if (j == v[n].size()) puts("IMPOSSIBLE");
    }
    
    return 0;
}
