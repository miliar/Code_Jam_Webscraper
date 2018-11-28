#include<cstdio>

using namespace std;

int K, S, C;

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    scanf ("%d %d %d", &K, &S, &C);
    for (int i=1; i<=K; i++)
        printf ("%d ", i);
    printf ("\n");
}

return 0;
}
