#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
using namespace std;

typedef pair<char, int> pair_t;

int TC, N, M;
char line[105];
vector<pair_t> canonical[105];

vector<pair_t> convert(char S[]) {
    int len = strlen(S);
    int pivot = 0;
    int ii = 0;
    vector<pair_t> result;
    while (pivot < len) {
        while (ii < len && S[ii] == S[pivot])
            ii++;
        result.push_back(make_pair(S[pivot], ii - pivot));
        pivot = ii;
    }
    return result;
}

int main() {
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        scanf("%d", &N);
        M = 0;
        for (int i = 0; i < N; i++) {
            scanf("%s", line);
            canonical[i] = convert(line);
            // for (int j = 0; j < (int)canonical[i].size(); j++)
            //     printf("(%c, %d) ", canonical[i][j].first, canonical[i][j].second);
            // printf("\n");
            M = ((int)canonical[i].size() > M) ? canonical[i].size() : M;
        }

        bool possible = true;
        int cost = 0;
        for (int j = 0; j < M && possible; j++) {
            int avg = 0;
            for (int i = 0; i < N; i++) {
                if (canonical[i].size() < M) {
                    possible = false;
                    break;
                }
                if (canonical[i][j].first != canonical[0][j].first) {
                    possible = false;
                    break;
                }
                avg += canonical[i][j].second;
            }
            if (possible) {
                avg /= N;
                for (int i = 0; i < N; i++) {
                    if (canonical[i][j].second > avg)
                        cost += canonical[i][j].second - avg;
                    else
                        cost += avg - canonical[i][j].second;
                }
            }
        }
        printf("Case #%d: ", tc);
        if (possible)
            printf("%d\n", cost);
        else
            puts("Fegla Won");
    }
}