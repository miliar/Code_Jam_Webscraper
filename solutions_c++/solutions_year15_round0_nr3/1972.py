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

const int MAX = 11000;
const int MAXC = 15;
const int INF = 1e9;
const int MOD = 1000000007;
const double EPS = 1e-11;

int arr[5][5] = {{0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

int n, m;
string str;
int cur[MAX];
int all[MAX];

int mul(int a, int b)
{
    if(a < 0 && b < 0 || a > 0 && b > 0)
        return arr[abs(a)][abs(b)];
    return -arr[abs(a)][abs(b)];
        
}

bool mx()
{
    all[n - 1] = cur[n - 1];
    for(int i = n - 2; i >= 0; --i)
    {
        all[i] = mul(cur[i], all[i + 1]);
    }
    
    //for(int i = 0; i < n; ++i)
    //    cout << all[i] << ' ';
    //cout << endl;
    
    int summ = 1;
    for(int i = 0; i < n - 2; ++i)
    {
        summ = mul(summ, cur[i]);
        if(summ != 2)
            continue;
        int sumj = 1;
        
        for(int j = i + 1; j < n - 1; ++j)
        {
            sumj = mul(sumj, cur[j]);
            if(sumj == 3 && all[j + 1] == 4)
                return true;
        }
    }
    return false;
}


int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int ti = 1; ti <= t; ++ti)
    {
        cin >> n >> m >> str;
        string temp = "";
        for(int i = 0; i < m; ++i)
            temp += str;
        str = temp;
        n *= m;
        for(int i = 0; i < n; ++i)
        {
            if(str[i] == 'i')
                cur[i] = 2;
            else if(str[i] == 'j')
                cur[i] = 3;
            else
                cur[i] = 4;
        }
        bool answ = mx();
        if(answ)
            cout << "Case #" << ti << ": YES\n";
        else
            cout << "Case #" << ti << ": NO\n";
    }
}
