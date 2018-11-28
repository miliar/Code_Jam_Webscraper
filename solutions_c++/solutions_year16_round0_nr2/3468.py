# include <string>
# include <vector>
# include <iostream>
# include <sstream>
# include <cstdio>
# include <cstdlib>
# include <cmath>
# include <cctype>
# include <cstring>
# include <map>
# include <queue>
# include <deque>
# include <set>
# include <algorithm>
# include <utility>
# include <functional>
# include <stack>
# include <bitset>
# include <complex>
# include <cassert>
# include <ctime>
# include <list>
# include <valarray>

using namespace std;

int dp[200][200][2][2];
bool visited[200][200][2][2];

vector<int> arr;

int test(int start, int end, int required, int reversed)
{
    if(start == end)
    {
        if(reversed == 1)
        {
            if(1 - arr[start] == required)
            {
                return 0;
            }
            else return 1;
        }
        else
        {
            if(arr[start] == required)
            {
                return 0;
            }
            else return 1;
        }
    }
    
    if(dp[start][end][required][reversed] != -1)
        return dp[start][end][required][reversed];
    
    visited[start][end][required][reversed] = true;
    
    int res = 1e8;
    
    if(reversed == 0)
    {
        if(arr[end] == required)
            return dp[start][end][required][reversed] = test(start, end - 1, required, reversed);
    }
    else
    {
        if((1 - arr[start]) == required)
            return dp[start][end][required][reversed] = test(start + 1, end, required, reversed);
    }
    
    if(reversed == 0)
    {
        for(int k = start; k < end; k++)
        {
            int tmp = test(start, k, 0, 0) + 1 + test(k + 1, end, 1, 1);
            res = min(res, tmp);
        }
    }
    else
    {
        for(int k = end; k > start; k--)
        {
            int tmp = test(k, end, 0, 1) + 1 + test(start, k - 1, 1, 0);
            res = min(res, tmp);
        }
    }
    
    dp[start][end][required][reversed] = res;
    
    // flip whole range and test..
    return dp[start][end][required][reversed] = min(res, 1 + test(start, end, required, 1 - reversed));
}
int main()
{
    int t;
    cin >> t;
    
    int index = 1;
    while(--t>=0)
    {
        string s;
        cin >> s;
        
        arr = vector<int>();
        
        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '-')
                arr.push_back(0);
            else arr.push_back(1);
        }
        
        memset(&dp, -1, sizeof(dp));
        memset(&visited, 0, sizeof(visited));
        
        int res = test(0, arr.size() - 1, 1, 0);
        
        cout << "Case #" << index++ << ": " << res << endl;
    }
    return 0;
}

