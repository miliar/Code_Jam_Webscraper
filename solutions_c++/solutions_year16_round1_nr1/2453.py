#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;


int main()
{
    ifstream f1("A-large(1).in");
    ofstream f2("A-large(1).out");
    int T;
    f1 >> T;
    string s;
    string ans;
    char first_letter;
    int n;
    bool where[1005];
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        f1 >> s;
        memset(where, false, sizeof where);
        n = s.size();
        first_letter = 0;
        for(int i = 0; i < n; ++i)
        {
            if(s[i] >= first_letter)
            {
                first_letter = s[i];
                where[i] = true;
            }
        }
        ans = "";
        for(int i = 0; i < n; ++i)
            if(where[i] == 1)
                ans += s[i];
        reverse(ans.begin(), ans.end());
        for(int i = 0; i < n; ++i)
            if(where[i] == 0)
                ans += s[i];
        f2 << ans << endl;
    }
    return 0;
}

