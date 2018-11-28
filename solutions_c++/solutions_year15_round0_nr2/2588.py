#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

int n;
int p[1000];

int run()
{
    int m = -1;
    cin >> n;
    memset(p, 0, sizeof(p));
    int t;
    for (int i = 0; i < n; i += 1)
    {
        cin >> t;
        p[t] += 1;
        m = max(m, t);
    }

    int res = m;
    for (int i = 1; i < res; i += 1)
    {
        int c = i;
        for (int j = i+1; j <= m; j += 1)
        {
            c += p[j] * (j / i + (j % i == 0 ? -1 : 0));
        }
        res = min(res, c);
    }
    return res;
}

int main()
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i += 1)
    {
        cout << "Case #" << (i+1) << ": " << run() << "\n";
    }
}
