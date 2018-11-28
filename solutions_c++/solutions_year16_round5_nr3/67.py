#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const double inf = 1e20;

struct Point
{
    double x, y, z;
};

inline Point operator - (Point a, Point b)
{
    return Point{a.x - b.x, a.y - b.y, a.z - b.z};
}

inline double operator * (Point a, Point b)
{
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

const int maxN = 1000;
int n;
double s;
Point p[maxN], v[maxN];
double t1[maxN][maxN], t2[maxN][maxN];

struct Event
{
    int from;
    int to;
    double time;
    bool enable;
};

bool operator < (const Event& a, const Event& b)
{
    return a.time < b.time;
}

bool possible(double lmt)
{
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < n; j ++)
        {
            double a = (v[i] - v[j]) * (v[i] - v[j]);
            double b = (v[i] - v[j]) * (p[i] - p[j]);
            double c = (p[i] - p[j]) * (p[i] - p[j]) - lmt * lmt;

            if (a < 1e-8)
            {
                if ((p[i] - p[j]) * (p[i] - p[j]) <= lmt * lmt)
                {
                    t1[i][j] = 0;
                    t2[i][j] = inf;
                }
                else
                {
                    t1[i][j] = -1;
                    t2[i][j] = -1;
                }
            }
            else if (b < 0)
            {
                t1[i][j] = -1;
                t2[i][j] = -1;
            }
            else
            {
                double b24ac = sqrt(b * b - 4 * a * c);
                t1[i][j] = (-b-b24ac) / (2*a);
                t2[i][j] = (-b+b24ac) / (2*a);
            }
        }

    vector<Event> event;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j ++)
        {
            if (t1[i][j] >= 0 && t1[i][j] < inf)
            {
                event.push_back(Event({i, j, t1[i][j], true}));
            }
            if (t2[i][j] >= 0 && t2[i][j] < inf)
            {
                event.push_back(Event({i, j, t2[i][j], true}));
            }
        }
    sort(event.begin(), event.end());

    bool vst[n];
    int deg[n];
    for (int i = 0; i < n; i ++)
    {
        deg[i] = 0;
        vst[i] = false;
    }
    for (int i = 0; i < n; i ++)
        for (int j = i + 1; j < n; j ++)
            if (t1[i][j] <= 0 && 0 <= t2[i][j])
            {
                deg[i] ++;
            }
    {
        queue<int> q;
        q.push(0);
        vst[0] = true;

        while (!q.empty())
        {
            int x = q.front();
            q.pop();

            for (int i = 0; i < n; i ++)
                if (!vst[i] && t1[x][i] <= 0 && 0 <= t2[x][i])
                {
                    q.push(i);
                    vst[i] = true;
                }
        }
    }

    if (vst[1])
    {
        return true;
    }
    return false;
}

int main()
{
    int ct, t;
    scanf("%d", &ct);

    for (t = 1; t <= ct; t ++)
    {
        scanf("%d%lf", &n, &s);
        for (int i = 0; i < n; i ++)
        {
            scanf("%lf%lf%lf%lf%lf%lf",
                    &p[i].x, &p[i].y, &p[i].z,
                    &v[i].x, &v[i].y, &v[i].z
                    );
        }

        double l = 0;
        double r = 1e9;
        while (r - l >= 1e-8)
        {
            double m = (l + r) / 2;
            if (possible(m))
            {
                r = m;
            }
            else
            {
                l = m;
            }
        }
        printf("Case #%d: %.8lf\n", t, (l + r) / 2);
    }
    return 0;
}
