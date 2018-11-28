#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    freopen ("in.txt", "r", stdin);
    freopen ("Cshort.txt", "w", stdout);
    int t, a, b;
    cin >> t;
    bool V[1001];
    // ola k ase?
    memset(V, 0, sizeof(V));
    V[1] = 1;
    V[4] = 1;
    V[9] = 1;
    V[121] = 1;
    V[484] = 1;
    for (int k=1; k<=t; k++)
    {
        int ans = 0;
        cin >> a >> b;
        for (int i=a; i<=b; i++)
        {
            ans += V[i];
        }
        cout << "Case #" << k << ": " << ans << endl;
    }
    fclose (stdout);
    return 0;
}
