#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

string f(string const & s)
{
    if(s.empty())
        return s;

    char mx = *max_element(s.begin(), s.end());
    int first = 0, n =SZ(s);
    REP(i,n)if(s[i]==mx)
    {
        first = i;
        break;
    }

    deque<char> q;
    string res = f(s.substr(0, first));
    int i = first;
    while(i<n)
    {
        if(s[i]==mx)res.insert(res.begin(), s[i]);
        else res.push_back(s[i]);
        ++i;
    }

    return res;
}


void solve()
{
    string s,res;
    cin >> s;

    cout << f(s) << endl;
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    freopen("../data/A-large.in", "r", stdin);
    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
