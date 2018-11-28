#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int t, mmax;
    string s;

    cin >> t;
    for(int i=1; i <= t; ++i)
    {
        cin >> mmax >> s;
        int curStanding = 0, needBackup = 0;
        for(int j=0; j < s.size(); ++j)
        {
            if(s[j] > '0')
            {
                if(curStanding < j)
                {
                    needBackup += j - curStanding;
                    curStanding += needBackup;
                }
                curStanding += s[j] - '0';
            }
        }

        
        cout << "Case #" << i << ": " << needBackup << endl;
    }

    return 0;
}
