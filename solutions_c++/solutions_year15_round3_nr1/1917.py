#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cctype>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <map>
#include <bitset>
#include <stack>
/*  //c++11
#include <unordered_map>
#include <unordered_set>
#include <tuple>
*/

using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");

int res;
int n, m, w;



void solve()
{

    fin>>n>>m>>w;
    res = 0;
    res = m/w + w - 1 + (m%w!=0);
    res *= n;
    fout<<res;
}

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    int T;
    fin>>T;
    for(int i = 1; i <= T; i++)
    {
        fout<<"Case #"<<i<<": ";
        solve();
        fout<<'\n';
    }


    return 0;
}


//FILE!!!
