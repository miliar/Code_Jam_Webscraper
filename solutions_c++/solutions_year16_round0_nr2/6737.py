#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solve(string s)
{
    int ret = 0;
    
    for (int i = 0; i < s.size() - 1; i++)
        if (s[i] != s[i + 1])
            ret++;
    
    if (s[s.size() - 1] == '-')
        ret++;
    
    return ret;
}

int main()
{
    int T;
    string s;
    
    cin >> T;
    
    for (int test = 1; test <= T; test++)
    {
        cin >> s;
        
        cout << "Case #" << test << ": " << solve(s) << '\n';
    }
    
    return 0;
}