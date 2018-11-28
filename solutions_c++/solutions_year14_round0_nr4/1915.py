#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int n;
long double a[1000];
long double b[1000];

void leggi()
{
    cin >> n;
    for (int i = 0; i < n; i += 1)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i += 1)
    {
        cin >> b[i];
    }
    sort(a, a+n);
    sort(b, b+n);
}

int war()
{
    int result = 0;
    int j = 0;
    for (int i = n-1; i >= 0; i -= 1)
    {
        if (a[i] > b[n-1])
        {
            result += 1;
            j += 1;
        }
        else
        {
            break;
        }
    }
    set<long double> bs;
    for (int i = j; i < n; i += 1)
    {
        bs.insert(b[i]);
    }
    for (int i = 0; i < n-j; i += 1)
    {
        set<long double>::iterator low = bs.lower_bound(a[i]);
        if (low == bs.end())
        {
            result += 1;
            bs.erase(bs.begin());
        }
        else
        {
            bs.erase(low);
        }
    }
    return result;
}

int dwar()
{
    int j = 0;
    int result = 0;
    for (int i = 0; i < n; i += 1)
    {
        if (a[i] > b[j])
        {
            result += 1;
            j += 1;
        }
    }
    return result;
}

int main()
{
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i += 1)
    {
        leggi();
        cout << "Case #" << i << ": " << dwar() << ' ' << war() << endl;
    }
}
