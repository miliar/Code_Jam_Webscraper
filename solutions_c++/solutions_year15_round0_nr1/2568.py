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
ofstream fout("output.out");

string s;

void solve()
{
    int n;
    fin>>n;
    fin>>s;
    int res = 0;
    int currentSum = 0;
    for(int i = 0; i <= n; i++)
    {
        if(currentSum < i)
        {
            res += i - currentSum;
            currentSum = i;
        }
        currentSum += s[i]-'0';
    }
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
