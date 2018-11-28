#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

void solve_case(const int cn)
{
    int N;
    cin >> N;
    vector<int> v(N, 0);
    for(int i=0;i<N;++i)
    {
        cin >> v[i];
    }
    vector<int> s = v;
    sort(s.begin(), s.end());
    int out = 0;
    for(int i=0;i<N;++i)
    {
        int t=0;
        while(v[t] != s[i]){++t;}
        out += min(t, (N-i)-t-1);
        v.erase(v.begin() + t);
    }
    printf("Case #%d: %d\n", cn, out);
}

int main(int argc, char **argv)
{
    int CASES;
    cin >> CASES;
    for(int cn=1;cn<=CASES;++cn)
    {
        solve_case(cn);
    }
    return 0;
}
