#include <iostream>
#include <vector>

using namespace std;

const int inf = 1 << 30;

vector<int> a[1 << 11];
vector<int> c[1 << 11];
vector<int> r[1 << 11];
int last[1 << 11];
int in[1 << 11];
int level[1 << 11];
int q[1 << 11];

void add(int i, int j, int k)
{
//    cout << i << " " << j << endl;

    r[i].push_back(a[j].size());
    r[j].push_back(a[i].size());

    a[i].push_back(j);
    c[i].push_back(k);

    a[j].push_back(i);
    c[j].push_back(0);
}

int blockingFlowValue(int v, int t, int m)
{
    if (v == t)
        return m;

    int flowValue = 0;

    for (; last[v] < a[v].size(); last[v]++)
    {
        int u = a[v][last[v]];

        if (level[u] == level[v] + 1 && c[v][last[v]] > 0)
        {
            int w = blockingFlowValue(u, t, min(m - flowValue, c[v][last[v]]));
            c[v][last[v]] -= w;
            c[u][r[v][last[v]]] += w;
            flowValue += w;

            if (flowValue == m)
                return m;
        }
    }

    return flowValue;
}

int maximumFlowValue(int n, int s, int t)
{
    int flowValue = 0;

    for (;;)
    {
        for (int i=0; i<n; i++)
            level[i] = inf;

        level[s] = 0;

        int qs = 0, qf = 0;
        q[qf++] = s;

        for (; qs < qf; qs++)
        {
            int v = q[qs];
            for (int i=0; i<a[v].size(); i++)
                if (c[v][i] > 0 && level[a[v][i]] == inf)
                {
                    q[qf++] = a[v][i];
                    level[a[v][i]] = level[v] + 1;
                }
        }

        if (level[t] == inf)
            return flowValue;

        for (int i=0; i<n; i++)
            last[i] = 0;

        flowValue += blockingFlowValue(s, t, inf);
    }

    return flowValue;
}

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;

        int s = n;
        int t = n+1;

        char w[1024];
        int x[1024];
        int y[2048] = {};
        int q = 1;

        for (int i=0; i<n; i++)
            cin >> w[i] >> x[i];

        for (int i=0; i<n; i++, q++)
            if (w[i] == 'L')
                for (int j=i-1; j>=0; j--)
                {
                    if (y[x[j]] == q)
                        continue;
                    if (x[j])
                        y[x[j]] = q;
                    if (w[j] == 'E' && (!x[i] || !x[j] || x[i] == x[j]))
                        add(j, i, 1);
                    if (w[j] == 'L' && x[i] == x[j] && x[i])
                        break;
                }

        for (int i=0; i<n; i++)
            if (w[i] == 'E')
                add(s, i, 1);
            else
                add(i, t, 1);

        int L = 0;
        for (int i=0; i<n; i++)
            L += w[i] == 'L';
/*
            for (int i=0; i<n+2; i++)
            {
                for (int j=0; j<a[i].size(); j++)
                    if (c[i][j])
                        cout << a[i][j] << " ";
                cout << endl;
            }
            cout << endl;
*/
        int f1 = maximumFlowValue(n+2, s, t);
/*
            for (int i=0; i<n+2; i++)
            {
                for (int j=0; j<a[i].size(); j++)
                    if (c[i][j])
                        cout << a[i][j] << " ";
                cout << endl;
            }
            cout << endl;
*/
        {
            bool y[2048] = {};

            for (int i=0; i<n; i++)
            {
                if (w[i] == 'L' && !y[x[i]])
                    add(s, i, 1);
                if (x[i])
                    y[x[i]] = 1;
            }
        }
/*
            for (int i=0; i<n+2; i++)
            {
                for (int j=0; j<a[i].size(); j++)
                    if (c[i][j])
                        cout << a[i][j] << " ";
                cout << endl;
            }
*/
        int f2 = f1 + maximumFlowValue(n+2, s, t);

        for (int i=0; i<n+2; i++)
        {
            a[i].clear();
            c[i].clear();
            r[i].clear();
        }

        for (int i=0; i<n; i++, q++)
            if (w[i] == 'L')
                for (int j=i-1; j>=0; j--)
                {
                    if (y[x[j]] == q)
                        continue;
                    if (x[j])
                        y[x[j]] = q;
                    if (w[j] == 'E' && (!x[i] || !x[j] || x[i] == x[j]))
                        add(j, i, 1);
                    if (w[j] == 'L' && x[i] == x[j] && x[i])
                        break;
                }

        for (int i=0; i<n; i++)
            if (w[i] == 'E')
                add(s, i, 1);
            else
                add(i, t, 1);

        {
            bool y[2048] = {};

            for (int i=n-1; i>=0; i--)
            {
                if (w[i] == 'E' && !y[x[i]])
                    add(i, t, 1);
                if (x[i])
                    y[x[i]] = 1;
            }
        }
/*
            for (int i=0; i<n+2; i++)
            {
                for (int j=0; j<a[i].size(); j++)
                    if (c[i][j])
                        cout << a[i][j] << " ";
                cout << endl;
            }
*/
        int f3 = maximumFlowValue(n+2, s, t);

        for (int i=0; i<n+2; i++)
        {
            a[i].clear();
            c[i].clear();
            r[i].clear();
        }

//        cout << f1 << " " << f2 << " " << f3 << endl;

        cout << "Case #" << tt << ": ";
        if (f2 < L || f3 < n - L)
            cout << "CRIME TIME" << endl;
        else
            cout << n - L - f1 << endl;
    }

    return 0;
}
