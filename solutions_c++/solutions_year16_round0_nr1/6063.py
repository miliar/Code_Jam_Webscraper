#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
typedef unsigned long long ull;
using namespace std;

set<int> digits(int n)
{
    set<int> res;
    while(n != 0)
    {
        res.insert(n % 10);
        n /= 10;   
    }
    return res;
}

void solve(int t, int n)
{
    if (n == 0)
    {
        cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
        return;
    }
    ull cur = n;
    vector<int> was(10, 0);
    int i;
    for (i = 1; ;++i)
    {
        set<int> a = digits(cur);
        for (set<int>::const_iterator it = a.begin(); it != a.end(); ++it)
            was[*it] = 1;
        int sum = 0;
        for (int i = 0; i < 10; ++i)
            sum += was[i];
        if (sum == 10)
        {
            cout << "Case #" << t + 1 << ": " << cur << endl;
            return;
        }
        cur += n;
        //cout << cur << endl;
    }
}

int main()
{
    int t, n;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n;   
        solve(i, n);
    }
}
