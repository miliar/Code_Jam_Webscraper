#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>

using namespace std;


int keta(long long n)
{
    int cnt = 0;
    while (n > 0) {
        cnt++;
        n /= 10;
    }

    return cnt;
}

long long solve(long long n)
{
    if (n == 0)
        return -1;
    int ket = keta(n);

    vector<bool> list(10, false);
    int cnt = 0;
    for (int i = 1; i <= 1000000; i++)
    {
        long long t = i * n;
        while (t > 0)
        {
            int temp = t % 10;
            if (!list[temp])
            {
                list[temp] = true;
                cnt++;
            }
            if (cnt == 10)
                return i * n;

            t /= 10;
        }
    }

    return -1;
    

}
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        int res = solve(n);
        printf("Case #%d: ", i + 1);
        if (res == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << res << endl;

    }
    return 0;
}