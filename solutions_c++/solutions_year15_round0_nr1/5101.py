#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin ("/Programming/Sources/cf_c/cf_c/input.txt");
    ofstream cout ("/Programming/Sources/cf_c/cf_c/output.txt");
    
    int i, j, n, m, k, t;
    
    cin >> t;
    for (int curtest = 1; curtest < t + 1; ++curtest)
    {
        string s;
        
        cin >> n;
        cin >> s;
        int ans = 0, acc = 0;
        for (j = 0; j < s.size(); j++)
        {
            if (s[j] - '0' == 0)
                continue;
            if (j > acc)
            {
                ans += j - acc;
                acc = j;
            }
            acc += s[j] - '0';
        }
        cout << "Case #" << curtest<< ": " << ans << endl;
    }
}