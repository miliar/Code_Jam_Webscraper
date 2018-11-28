#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;
ifstream in("C-large-1.in");
ofstream out("fair_square.out");
typedef long long ll;

vector<ll> f;

int pal(ll k)
{
    vector<int> c;
    while (k)
    {
        c.push_back(k%10);
        k /=10;
    }
    for (int i = 0; i < c.size()/2; ++i)
        if (c[i] != c[ c.size()-i-1 ] ) return 0;
    return 1;
}


int main()
{
    for (ll i = 0; i <= 1e7+100; ++i)
        if ( pal(i) && pal(i*i) ){
                f.push_back(i*i);
        }

    int n; in >> n;
    for (int i = 1; i <= n; ++i)
    {
        out << "Case #" << i << ": ";
        ll a,b; in >> a >> b;
        int k = 0;
        for (int j = 0; j < f.size(); ++j)
            if ( f[j] >= a && f[j] <= b ) ++k;
        out << k << '\n';
    }
    return 0;
}
