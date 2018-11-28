#include <cstdio>
#include <vector>
#include <string>
using namespace std;

const int inf = 128;
const int MAX = 128;
int lawn[MAX][MAX];

int main()
{
    freopen("bbig.in", "r", stdin);
    freopen("bbig.out", "w", stdout);

    int tests, row, col;

    scanf("%d", &tests);
    for (int case_no = 1; case_no <= tests; ++case_no)
    {
        printf("Case #%d: ", case_no);
        scanf("%d %d", &row, &col);

        for (int i=0; i<row; ++i)
            for (int j=0; j<col; ++j)
                scanf("%d", &lawn[i][j]);

        int minimum;

        bool good = true;

        while (true)
        {
            minimum = inf;
            for (int i=0; i<row; ++i)
                for (int j=0; j<col; ++j)
                    if (lawn[i][j] != 0)
                        minimum = min(minimum, lawn[i][j]);

            if (minimum == inf)
                break;

            bool found = false;

            // eliminate full rows
            for (int i=0; i<row; ++i)
            {
                bool ok = false;
                for (int j=0; j<col; ++j)
                {
                    if (lawn[i][j] == 0)
                        continue;
                    ok = true;
                    if (lawn[i][j] != minimum)
                    {
                        ok = false;
                        break;
                    }
                }

                if (ok)
                {
                    found = true;
                    for (int j=0; j<col; ++j)
                        lawn[i][j] = 0;
                }
            }

            // eliminate full cols
            for (int i=0; i<col; ++i)
            {
                bool ok = false;
                for (int j=0; j<row; ++j)
                {
                    if (lawn[j][i] == 0)
                        continue;
                    ok = true;
                    if (lawn[j][i] != minimum)
                    {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                {
                    found = true;
                    for (int j=0; j<row; ++j)
                        lawn[j][i] = 0;
                }
            }

            if (!found)
            {
                good = false;
                break;
            }
        }

        printf("%s\n", good ? "YES" : "NO");

    }
}
