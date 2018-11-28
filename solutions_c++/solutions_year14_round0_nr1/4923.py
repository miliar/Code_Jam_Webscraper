#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

const int N = 4;
int mat[N+1][N+1];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, r, cas = 0;
    scanf("%d", &t);

    while (t--){
        map<int, int> dic;
        vector<int> ans;

        scanf("%d", &r);
        for (int i = 1; i <= N; ++i)
            for (int j = 1; j <= N; ++j)
                scanf("%d", &mat[i][j]);
        for (int j = 1; j <= N; ++j) dic[mat[r][j]]++;
        scanf("%d", &r);
        for (int i = 1; i <= N; ++i)
            for (int j = 1; j <= N; ++j)
                scanf("%d", &mat[i][j]);
        for (int j = 1; j <= N; ++j)
            if (dic[mat[r][j]] == 1)
                ans.push_back(mat[r][j]);
        printf("Case #%d: ", ++cas);
        if (ans.size() == 0) printf("Volunteer cheated!\n");
        else if (ans.size() == 1) printf("%d\n", ans[0]);
        else printf("Bad magician!\n");
    }

    return 0;
}
