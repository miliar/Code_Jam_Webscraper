#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define EPS 1.0e-6
#define INF 10000000

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int n, x, s[10005];
    int I, J, cd;

    scanf("%d", &T);
    for(int ncaso=1; ncaso<=T; ncaso++)
    {
        scanf("%d%d", &n, &x);
        FOR(i,0,n) scanf("%d", &s[i]);
        sort(s, s+n);

        cd = 0, I=0, J=n-1;
        while(I<J)
        {
            if (s[I] + s[J] <= x)
            {
                cd++;
                I++;
                J--;
            }
            else
            {
                cd++;
                J--;
            }
        }
        if (I==J) cd++;

        printf("Case #%d: %d\n", ncaso, cd);
    }

    return 0;
}
