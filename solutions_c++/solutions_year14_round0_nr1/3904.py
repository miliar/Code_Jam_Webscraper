#include <cstdio>
#include <set>
#define MAXN 4

using namespace std;

int main()
{
    FILE *fin = fopen("A-small-attempt0.in", "r");
    FILE *fout = fopen("output.txt", "w");
    int t, a1, a2;
    int cards[MAXN][MAXN];
    set<int> row;
    set<int> sol;

    fscanf(fin, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        row.erase(row.begin(), row.end());
        sol.erase(sol.begin(), sol.end());
        fscanf(fin, "%d", &a1);
        for (int j = 0; j < MAXN; j++)
        {
            for (int k = 0; k < MAXN; k++)
            {
                fscanf(fin, "%d", &cards[j][k]);
            }
        }

        for (int j = 0; j < MAXN; j++)
        {
            row.insert(cards[a1-1][j]);
        }

        fscanf(fin, "%d", &a2);
        for (int j = 0; j < MAXN; j++)
        {
            for (int k = 0; k < MAXN; k++)
            {
                fscanf(fin, "%d", &cards[j][k]);
            }
        }

        for (int j = 0; j < MAXN; j++)
        {
            if (row.find(cards[a2-1][j]) != row.end())
            {
                sol.insert(cards[a2-1][j]);
            }
        }

        switch (sol.size())
        {
        case 0:
            fprintf(fout, "Case #%d: Volunteer cheated!\n", i);
            break;
        case 1:
            fprintf(fout, "Case #%d: %d\n", i, *sol.begin());
            break;
        default:
            fprintf(fout, "Case #%d: Bad magician!\n", i);
        }
    }

}
