#include <iostream>
#include <cstdio>

using namespace std;

bool gana (int x, int r, int c)
{
    if (x == 3 && r == 3 && c == 3) return false;
    if ((r*c) % x != 0) return true;
    if (x == 1) return false;
    if (x == 2)
    {
        if (r*c >= 2) return false;
        return true;
    }
    if (c == 1 || r == 1)
        return true;
    if (x == 3)
    {
        if ((c*r)%6 == 0)
            return false;
        return true;
    }
    if (r*c >= 12)
        return false;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, x, r, c;
    cin >> n;
    for (int tc=1; tc<=n; tc++)
    {
        cin >> x >> r >> c;
        cout << "Case #" << tc << ": " << (gana(x, r, c) ? "RICHARD" : "GABRIEL") << endl;
    }
    fclose(stdout);
    return 0;
}

/*
 (\_/)
 (. .)
 c(")(")
 */