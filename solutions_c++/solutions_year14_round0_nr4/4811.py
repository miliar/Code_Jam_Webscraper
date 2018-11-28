#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<iomanip>
#include<algorithm>
#include<set>
using namespace std;

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define N 120

double a[N], b[N], a1[N], b1[N];

int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("b.txt", "w", stdout);
    //freopen("a.txt","r",stdin);

    int T;
    cin>>T;
    FOR(kk, 1, T)
    {
        int n;
        cin>>n;
        FOR(i, 1, n)
        {
            cin>>a[i];
            a1[i] = a[i];
        }
        FOR(i, 1, n)
        {
            cin>>b[i];
            b1[i] = b[i];
        }

        sort(a1+1, a1+n+1);
        sort(b1+1, b1+n+1);

        int Max = -1;
        do
        {
            int tp = 0;
            FOR(i, 1, n)
            if (a1[i] > b[i])
                tp += 1;
            Max = max(Max, tp);
        }
        while (next_permutation(a1+1, a1+n+1));

        set<double> b2;
        int Normal = 0;
        FOR(i, 1, n)
        b2.insert(b[i]);

        set<double>::iterator it;
        FOR(i, 1, n)
        {
            it = b2.upper_bound(a[i]);
            if (it == b2.end())
                Normal ++;
            else
                b2.erase(it);
        }

        printf("Case #%d: %d %d\n", kk, Max, Normal);
    }

    //fclose(stdout);
    return 0;
}
