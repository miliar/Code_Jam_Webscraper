#include <algorithm>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
using namespace std;

const int MAXN = 20, MAXL = 1000;

int N;
char tmp[1000000];
int sent[MAXN][MAXL];
int NS[MAXN];
map<string, int> dict;
bool iseng[MAXN];
int weng[MAXN * MAXL], wfre[MAXN * MAXL], wcomm[MAXN * MAXL];

int calc()
{
    int NE = 0, NF = 0;

    for (int i = 0; i < N; ++i)
        for (size_t j = 0; j < NS[i]; ++j)
            if (iseng[i]) weng[NE++] = sent[i][j]; else wfre[NF++] = sent[i][j];

    sort(weng, weng + NE);
    NE = unique(weng, weng + NE) - weng;
    sort(wfre, wfre + NF);
    NF = unique(wfre, wfre + NF) - wfre;

    return set_intersection(weng, weng + NE, wfre, wfre + NF, wcomm) - wcomm;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d\n", &N);
        dict.clear();
        int NW = 0;

        for (int i = 0; i < N; ++i) {
            NS[i] = 0;

            gets(tmp);
            istringstream is(tmp);

            string word;
            while (is >> word) {
                if (!dict.count(word)) dict[word] = NW++;
                sent[i][NS[i]++] = dict[word];
            }
            sort(sent[i], sent[i] + NS[i]);
        }

        iseng[0] = true; iseng[1] = false;
        int answer = 1000000000;

        for (int mask = 0; mask < (1 << (N - 2)); ++mask) {
            for (int i = 0; i < N - 2; ++i)
                iseng[i + 2] = ((mask & (1 << i)) != 0);

            int res = calc();
            answer = min(answer, res);
        }

        printf("Case #%d: %d\n", t + 1, answer);
    }

    return 0;
}
