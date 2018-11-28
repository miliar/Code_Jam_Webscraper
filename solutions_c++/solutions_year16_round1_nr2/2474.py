#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define RI(x) scanf("%d", &x)
#define RL(x) scanf("%I64d", &x)
#define RD(x) scanf("%f", &x)

vector<int> a[200];
vector<vector<int> > v;
int b[200][200];
bool used[200];
int cur;
int n;

void solve(int case_number)
{
    for (int i=0; i<200; ++i)
        used[i] = false;
    int x;
    cin >> n;
    for (int i=0; i<2*n-1; ++i)
    {
        a[i].clear();
        for (int j=0; j<n; ++j)
        {
            cin >> x;
            a[i].pb(x);
        }
    }
    int mn, ind1, ind2;
    int index;
    v.clear();
    for (int p=0; p<n; ++p)
    {
        mn = INT_MAX;
        ind1 = -1;
        ind2 = -1;
        for (int i=0; i<2*n-1; ++i)
        {
            if (!used[i])
                mn = min(mn, a[i][p]);
        }
        for (int i=0; i<2*n-1; ++i)
        {
            if (a[i][p] == mn)
            {
                if (ind1 == -1)
                    ind1 = i;
                else
                    ind2 = i;
                used[i] = true;
            }
        }
        if (ind2 == -1)
        {
            index = ind1;
            cur = p;
            for (int k=0; k<n; ++k)
                b[p][k] = a[ind1][k];
            v.pb(a[ind1]);
            v.pb(a[ind1]);
        }
        else
        {
            v.pb(a[ind1]);
            v.pb(a[ind2]);
        }
    }
    bool ok;
    for (int i=0; i < (1 << (2*n-1)); ++i)
    {
        for (int j=0; j<n; ++j)
        {
            if (j == cur)
                continue;
            if (i & (1 << j))
                ind1 = 2*j + 1;
            else
                ind1 = 2*j;
            for (int k=0; k<n; ++k)
                b[j][k] = v[ind1][k];
        }
        ok = true;
        for (int j=0; j<n; ++j)
        {
            if (j == cur)
                continue;
            if (i & (1 << j))
                ind1 = 2*j;
            else
                ind1 = 2*j + 1;
            for (int k=0; k<n; ++k)
                ok = ok && (b[k][j] == v[ind1][k]);
        }
        if (ok)
            break;
    }
    vector<int> temp;
    for (int i=0; i<n; ++i)
        temp.pb(b[cur][i]);
    if (v[2*cur] == temp)
    {
        temp.clear();
        for (int i=0; i<n; ++i)
            temp.pb(b[i][cur]);
    }

    cout << "Case #" << case_number << ": ";
    for (int i=0; i<n; ++i)
        cout << temp[i] << ' ';
    cout << "\n";
}

int main()
{
    freopen("input2.in", "r", stdin);
    freopen("output2.out", "w", stdout);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)
        solve(i);

    return 0;
}

