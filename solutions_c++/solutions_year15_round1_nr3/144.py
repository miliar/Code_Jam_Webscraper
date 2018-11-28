#include<cmath>
#include<iostream>
#include<algorithm>
#include<unistd.h>
using namespace std;

int n;
long long x[3000];
long long y[3000];

int pivot;
int idx[3000];

bool is_left_turn (int i, int j, int k)
{
    return (x[j] - x[i]) * (y[k] - y[i]) > (y[j] - y[i]) * (x[k] - x[i]);
}

bool is_right_turn (int i, int j, int k)
{
    return (x[j] - x[i]) * (y[k] - y[i]) < (y[j] - y[i]) * (x[k] - x[i]);
}

bool my_lt (int a, int b)
{
    double ang_a = atan2(y[a] - y[pivot], x[a] - x[pivot]);
    double ang_b = atan2(y[b] - y[pivot], x[b] - x[pivot]);
    if (abs(ang_a - ang_b) > 1e-3)
        return ang_a < ang_b;
    else
        return is_left_turn(pivot, a, b);
}

int run(int j)
{
    pivot = j;
    //cerr << x[pivot] << ' ' << y[pivot] << endl;
    for (int i = 0; i < n-1; i += 1)
    {
        idx[i] = (i < pivot ? i : i+1);
        //cerr << i << ' ' << idx << ' ' << ang << endl;
    }
    sort(idx, idx+n-1, my_lt);

    /*for (int j = 0; j < n-1; j += 1)
    {
        cout << pnts[j].second << '(' << x[pnts[j].second] << ' ' << y[pnts[j].second] << ' ' << pnts[j].first << ") ";
    }
    cout << endl;*/

    // sliding window
    int l = 0;
    int r = 1;
    int res = n-1;
    while (l < n-1)
    {
        //cerr << "between " << l << " and " << r << " it's " << dist(l, r) << endl;
        if (l != r && is_right_turn(idx[l], pivot, idx[r]))
        {
            //cerr << "enlarging" << endl;
            r = (r + 1) % (n-1);
            //sleep(1);
        }
        else
        {
            //cerr << "shrinking" << endl;
            int foo = ((r + (n-1) - l) % (n-1) + (n-1)) % n;
            res = min(res, foo);
            l += 1;
        }
    }

    return res;
}

int main()
{
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i += 1)
    {
        cout << "Case #" << i << ":\n";
        cin >> n;
        for (int j = 0; j < n; j += 1)
        {
            cin >> x[j] >> y[j];
        }
        for (int j = 0; j < n; j += 1)
        {
            cout << (n < 3 ? 0 : run(j)) << '\n';
        }
    }
}
