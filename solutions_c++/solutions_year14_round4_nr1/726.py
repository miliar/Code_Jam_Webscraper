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
    int N,X;
    cin >> N;
    cin >> X;
    vector<int> v(N, 0);
    for(int i=0;i<N;++i)
    {
        cin >> v[i];
        v[i] *= -1;
    }
    multiset<int> s(v.begin(), v.end());
    int out = 0;
    while(!s.empty()) {
        ++out;
        int x = -1 * (*s.begin());
        s.erase(s.begin());
        int lookup = -1 * (X - x);
        multiset<int>::iterator iter = s.lower_bound(lookup);
        if(iter == s.end()){continue;}
        s.erase(iter);
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
