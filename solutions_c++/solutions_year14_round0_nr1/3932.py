#include <cstdio>
#include <cstring>
using namespace std;


bool ok[17];


void ask_question()
{
    int row; scanf("%d", &row);
    for (int i = 1; i <= 4; i++)
    {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if (row != i)
        {
            ok[a] = false;
            ok[b] = false;
            ok[c] = false;
            ok[d] = false;
        }
    }
}


void solve_case(int test_case)
{
    memset(ok, true, sizeof(ok));

    ask_question();
    ask_question();

    int solution = -1;
    bool two_solutions = false;
    for (int i = 1; i <= 16; i++)
    {
        if (ok[i])
        {
            if (solution != -1) two_solutions = true;
            solution = i;
        }
    }

    printf("Case #%d: ", test_case);
    if (solution == -1) puts("Volunteer cheated!");
    else if (two_solutions) puts("Bad magician!");
    else printf("%d\n", solution);
}


int main()
{
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve_case(t);

    return 0;
}
