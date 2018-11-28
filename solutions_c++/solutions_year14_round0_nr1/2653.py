#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int M[4][4];

set <int> A;
set <int> B;
set <int> ans;

int t;
void solve() {
    A.clear();
    B.clear();
    ans.clear();
    int i, j, r;

    scanf("%d", &r);
    for (i = 0; i < 4; ++i) 
        for (j = 0; j < 4; ++j) scanf("%d", &M[i][j]);
    for (j = 0; j < 4; ++j) A.insert(M[r - 1][j]);

    scanf("%d", &r);
    for (i = 0; i < 4; ++i) 
        for (j = 0; j < 4; ++j) scanf("%d", &M[i][j]);
    for (j = 0; j < 4; ++j) B.insert(M[r - 1][j]);

    for (auto ia = A.begin(); ia != A.end(); ++ia) {
        for (auto ib = B.begin(); ib != B.end(); ++ib) {
            if (*ia == *ib) ans.insert(*ia);
        }
    }
    printf("Case #%d: ", t);
    if (ans.size() == 1) printf("%d\n", *ans.begin());
    else if (ans.empty()) printf("Volunteer cheated!\n");
    else printf("Bad magician!\n");
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) solve();
    return 0;
}