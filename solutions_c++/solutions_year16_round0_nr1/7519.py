#include <iostream>
#include <fstream>
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
typedef long long int lli;
lli n,t,alt;
bool v[10];
bool stillnotall()
{
    for(int i = 0 ; i <= 9 ; i++)
        if (v[i] == false)
            return true;
    return false;
}
void add(lli nr)
{
    while(nr !=0)
    {
        v[nr%10] = true;
        nr /= 10;
    }
}
void solve()
{
    if( n == 0)
    {
        out<<"Case #"<<alt<<": INSOMNIA"<<'\n';
        return;
    }
    for(int i = 0 ; i<= 9 ; i++)
        v[i] = false;
    lli ixn,ii = 0;
    while(stillnotall())
    {
        ii++;
        ixn = ii*n;
        add(ixn);
    }
    out<<"Case #"<<alt<<": "<<ixn<<'\n';
}
int main()
{

    in >> t;
    for(alt = 1 ; alt <= t ; alt++)
    {
        in >> n;
        solve();
    }

    return 0;
}
