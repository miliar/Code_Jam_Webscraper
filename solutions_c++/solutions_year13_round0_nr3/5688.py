//C
#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

bool ispalin[1005];
bool isnum[1005];

int main()
{
    freopen("/home/zhj/Documents/C-small-attempt0.in", "r", stdin);
    freopen("/home/zhj/Documents/C-small-attempt0.out", "w", stdout);

    memset(ispalin, 0, sizeof(ispalin));
    for (int val = 1; val <= 1000; val++)
    {
        vector <int> vec;
        int x = val;
        while (x)
        {
            vec.push_back(x % 10);
            x /= 10;
        }
        int i = 0;
        int j = vec.size()-1;
        while (i < j && vec[i] == vec[j])
        {
            i++;
            j--;
        }
        if (i >= j)
        {
            ispalin[val] = true;
            //cout << val << endl;
        }
    }

    memset(isnum, 0, sizeof(isnum));
    for (int i = 1; i <= 1000; i++)
    {
        int sq = sqrt(i);
        if (sq * sq == i && ispalin[sq] && ispalin[i])
        {
            isnum[i] = true;
        }
    }

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        int A, B;
        cin >> A >> B;
        int cnt = 0;
        for (int i = A; i <= B; i++)
        {
            if (isnum[i])
            {
                cnt++;
            }
        }
        cout << "Case #" << cas << ": " << cnt << endl;
    }
    return 0;
}
