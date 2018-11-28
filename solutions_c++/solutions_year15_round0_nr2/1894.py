#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

const int MAX = 1100;
const int MAXC = 15;
const int INF = 1e9;
const int MOD = 1000000007;
const double EPS = 1e-11;

int arr[MAX];
int n;

int mx()
{
    sort(arr, arr + n);
    int out = INF;
    for(int i = 1; i <= arr[n - 1]; ++i)
    {
        int sum = 0;
        int mx = 0;
        for(int j = 0; j < n; ++j)
        {
            //cout << i << "!" << j << "!" << arr[i] << ' ';
            if(arr[j] <= i)
            {
                mx = max(arr[j], mx);
                continue;
            }
            
            int cur = arr[j] / i;
            if(arr[j] % i != 0)
                cur += 1;
            int cmx = arr[j] / cur;
            if(arr[j] % i != 0)
                cmx += 1;
            cur -= 1;
            // cout << cur << ' ' << cmx << ' ' << endl;
            
            sum += cur;
            mx = max(cmx, mx);
        }
        out = min(out, sum + mx);
        //cout << endl;
    }
    
    return out;
}


int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        cin >> n;
        for(int j = 0; j < n; ++j)
            cin >> arr[j];
        int answ = mx();
        cout << "Case #" << i << ": " << answ << '\n';
    }
}
