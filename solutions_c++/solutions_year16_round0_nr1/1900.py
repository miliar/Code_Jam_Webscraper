#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void set_digits(int n, vector<bool>& mrk)
{
    while(n > 0)
    {
        mrk[n % 10] = true;
        n /= 10;
    }
}

int calc(int n)
{
    int m = n;
    vector<bool> mrk(10, false);
    set_digits(m, mrk);
    while(find(mrk.begin(), mrk.end(), false) != mrk.end())
    {
        m += n;
        set_digits(m, mrk);
    }

    return m;
}

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        int n;
        cin >> n;
        cout << "Case #" << lp << ": ";
        if (n == 0)
        {
            cout << "INSOMNIA\n";
        }
        else
        {
            cout << calc(n) << "\n";
        }
    }

    return 0;
}
