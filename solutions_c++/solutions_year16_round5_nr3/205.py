#include<iostream>
using namespace std;

const int MAXN = 1000;
int x[MAXN], y[MAXN], z[MAXN], vx[MAXN], vy[MAXN], vz[MAXN], n;
double gr[MAXN][MAXN];
bool visited[MAXN];

void dfs(int curr, double dist)
{
    visited[curr] = true;
    for (int i = 0; i < n; i++)
        if (!visited[i] && gr[curr][i] <= dist)
            dfs(i, dist);
}

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        int s;
        cin >> n >> s;
        for (int i = 0; i < n; i++)
            cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
        double lo = 0, hi = 0, mid;
        int times = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                double dx = x[i] - x[j];
                double dy = y[i] - y[j];
                double dz = z[i] - z[j];
                gr[i][j] = gr[j][i] = sqrt(dx * dx + dy * dy + dz * dz);
                if (gr[i][j] > hi) hi = gr[i][j];
            }
        }
        while (fabs(hi - lo) > 1e-6 && times < 100)
        {
            times++;
            memset(visited, 0, sizeof(visited));
            mid = (lo + hi) / 2;
            dfs(0, mid);
            if (visited[1]) hi = mid;
            else lo = mid;
        }
        printf("Case #%d: %.6lf\n", ++kase, lo);
    }
    return 0;
}