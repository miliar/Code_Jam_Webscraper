#include <iostream>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

int n, p, r, s;
string combine(const string &s1, const string &s2) {
    if (s1 > s2)
        return s2 + s1;
    else
        return s1 + s2;
}
string build(char c, int depth)
{
    if (depth == 1)
        return string(1, c);
    if (c == 'P')
        return combine(build('P', depth - 1) , build('R', depth - 1));
    else if (c == 'R')
        return combine(build('R', depth - 1) , build('S', depth - 1));
    else if (c == 'S')
        return combine(build('P', depth - 1) , build('S', depth - 1));
    exit(233);
}
bool check(const string &str, int r, int p,int s)
{
    int rc = 0 , pc = 0, sc = 0;
    for (auto it = str.begin () ; it != str.end() ; ++it)
        if (*it == 'P')
            ++ pc;
        else if (*it == 'R')
            ++ rc;
        else if (*it == 'S')
            ++ sc;
    return rc == r && pc == p && sc == s;

}
void process(int tc)
{

    cin >> n >> r >> p >> s;
    string s1 = build('P', n + 1);
    if (check(s1, r, p,s))
    {
        cout << "Case #" << tc << ": " << s1 << endl;
        return ;
    }
    s1 = build('R', n + 1);
    if (check(s1, r, p,s))
    {
        cout << "Case #" << tc << ": " << s1 << endl;
        return ;
    }
    s1 = build('S', n + 1);
    if (check(s1, r, p,s))
    {
        cout << "Case #" << tc << ": " << s1 << endl;
        return ;
    }
    cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
}
int main()
{
    int t = 0 ;
    cin >> t;
    for (int i = 1 ; i <= t ; ++i)
        process(i);
    return 0;
}
