#include <bits/stdc++.h>
using namespace std;

int t, kol;
bool used[20];

void f(long long x)
{
    //cout << "-- " << x << endl;
    while(x > 0)
    {
        long long k = x%10;
        if(used[k] == false)
        {
            //cout << k << ' ';
            kol++;
            used[k] = true;
        }
        x/=10;
    }
    //cout << endl;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        cout << "Case #" << q+1 << ": ";
        long long n;
        kol = 0;
        bool ff = false;
        for(int i = 0; i < 10; ++i)
            used[i] = false;
        cin >> n;
        long long x = 0;
        for(int i = 0; i <= 2000001; ++i)
        {
            x += n;
            f(x);
            if(kol == 10)
            {
                ff = true;
                cout << x << "\n";
                break;
            }
        }
        if(ff == false)
            cout << "INSOMNIA\n";
    }
}
