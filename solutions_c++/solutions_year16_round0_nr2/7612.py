#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
string s;
int v[150],alt,t;
void solve()
{
    int sol = 0;
    int nr= s.size()-1;
    for(int i = 1 ; i <= nr ; i++)
        if(s[i]!=s[i-1])
            sol++;
    if(s[nr] == '-')
        sol++;
    out<<"Case #"<<alt<<": "<<sol<<'\n';
}
int main()
{

    in >> t;
    for(alt = 1 ; alt <= t ; alt++)
    {
        in >> s;
        solve();
    }

    return 0;
}
