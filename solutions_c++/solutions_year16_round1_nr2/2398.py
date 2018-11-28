#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int n;
int l[110][60];
int map[60][2];
int ans[60];
int flag[110];

int compare(int *a, int *b)
{
    for (int i = 0; i < n; ++i)
        if (a[i] < b[i])
            return -1;
        else if (b[i] < a[i])
            return 1;
    return 0;
}

void swap(int *a, int *b)
{
    if (a==b)
        return;
    int t;
    for (int i = 0; i < n; ++i)
    {
        t = a[i];
        a[i] = b[i];
        b[i] = t;
    }
}

bool match(int x, int rc, int ln)
{
    for (int i = 0; i < x; ++i)
    {
        if (map[i][rc^1] == -1)
            continue;
        int t = l[map[i][rc^1]][x];
        if (t != l[ln][i])
            return false;
    }
    return true;
}

bool dfs(int x, int rc, bool missed)
{
    if (x == n)
    {
        for (int i = 0; i < n; ++i)
            if (map[i][0] == -1 || map[i][1] == -1)
            {
                int t = (map[i][0] == -1)?1:0;
                for (int j = 0; j < n; ++j)
                    ans[j] = l[map[j][t]][i];
                break;
            }
        return true;
    }

    for (int i = 0; i < 2*n - 1; ++i)
        if (flag[i] == 0 && match(x, rc, i) && (flag[i-1]>0 || compare(l[i], l[i-1])!= 0))
        {
            flag[i] = 1;
            map[x][rc] = i;
            if (rc == 1)
            {
                if (dfs(x+1, 0, missed))
                    return true;
            }
            else
            {
                if (dfs(x, 1, missed))
                    return true;
            }
            flag[i] = 0;
        }
    if (!missed)
    {
        map[x][rc] = -1;
        if (rc == 1)
        {
            if (dfs(x+1, 0, true))
                return true;
        }
        else
        {
            if (dfs(x, 1, true))
                return true;
        }

    }
    return false;

}

bool check()
{
    for (int i = 0; i < n; ++i)
    {
        if (map[i][0]==-1)
            continue;
        for (int j = 0; j < n; ++j)
        {
            if (map[j][1] == -1)
                continue;
            if (l[map[i][0]][j] != l[map[j][1]][i])
                return false;
        }
    }
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TT;
    cin >> TT;
    for (int T = 1; T <= TT; ++T)
    {
        cin >> n;
        for (int i = 0; i < 2*n - 1; ++i)
            for (int j = 0; j < n; ++j)
                cin >> l[i][j];
        memset(map, 0, sizeof(map));
        memset(flag, 0, sizeof(flag));
        for (int i = 0; i < 2*n-1; ++i)
            for (int j = i+1; j < 2*n-1; ++j)
                if (compare(l[i], l[j])>0)
                    swap(l[i], l[j]);
        if (l[0][0] == l[1][0])
        {
            map[0][0] = 0;
            map[0][1] = 1;
            flag[0] = flag[1] = 1;
            dfs(1, 0 , false);
        }
        else
        {
            map[0][0] = 0;
            map[0][1] = -1;
            flag[0] = 1;
            dfs(1, 0, true);
        }

        if (!check())
        {
            cerr << "Error!" << " " << T << endl;
        }

        cout << "Case #" << T << ":";
        for (int i = 0 ; i < n; ++i)
            cout << " " << ans[i];
        cout << endl;
    }

    fclose(stdout);
    fclose(stdout);
    return 0;
}
