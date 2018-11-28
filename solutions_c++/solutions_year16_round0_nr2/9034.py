#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int k, i, j;
    vector <string> req;
    cin >> k;
    req.resize(k);
    for(i = 0; i < k; i++)
        cin >> req[i];
    for(i = 0; i < k; i++)
    {
        int cnt = 0;
        j = 0;
        if(req[i][0] == '-')
        {
            cnt++;
            while(j < req[i].size() and req[i][j] == '-')
                j++;
        }
        while(j < req[i].size())
        {
            if(req[i][j] == '-')
            {
                cnt += 2;
                while(j < req[i].size() and req[i][j] == '-')
                    j++;
            }
            j++;
        }
        cout << "Case #" << i + 1 << ": " << cnt << "\n";
    }
    return 0;
}
