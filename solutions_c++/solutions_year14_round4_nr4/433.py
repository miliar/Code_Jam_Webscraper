#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;

const int MAXN = 10;

int N, M;
vector<int> qq[MAXN];
char S[10][100];

int cur, mx, cnt;

struct Node
{
    Node* link[26];
    Node() { for (int i = 0; i < 26; ++i) link[i] = 0; }
};

void add(Node *T, char* S, char *L)
{
    if (S == L) return;

    if (T->link[S[0]-'A'] == 0) {
        T->link[S[0]-'A'] = new Node();
        ++cur;
    }

    add(T->link[S[0]-'A'], S+1, L);
}

void gen(int d)
{
    if (d == M) {
        for (int i = 0; i < N; ++i)
            if (qq[i].empty()) return;

        cur = 0;

        for (int i = 0; i < N; ++i) {
            ++cur;
            Node* root = new Node();

            for (int j = 0; j < qq[i].size(); ++j) {
                int L = strlen(&S[qq[i][j]][0]);
                for (int k = 0; k < L; ++k)
                    add(root, &S[qq[i][j]][0], &S[qq[i][j]][0]+k+1);
            }
        }

        if (cur > mx) {
            mx = cur; cnt = 1;
        } else if (cur == mx) {
            ++cnt;
        }

        return;
    }

    for (int i = 0; i < N; ++i) {
        qq[i].push_back(d);
        gen(d+1);
        qq[i].pop_back();
    }
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        scanf("%d%d", &M, &N);

        for (int i = 0; i < M; ++i) scanf("%s", &S[i][0]);

        mx = -1; gen(0);
        printf("%d %d\n", mx, cnt);
    }

    return 0;
}
