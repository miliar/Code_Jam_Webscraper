#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}

LL get_second_factor(LL num)
{
    for(LL i = 2; i * i <= num; i++)
    {
        if(num % i == 0)
            return i;
    }
    return num;
}

int main()
{
    int t, cas = 1;
    cin >> t;
    while(t--)
    {
        int n, m;
        cin >> n >> m;
        LL factors[11];
        cout << "Case #" << cas++ << ":" << endl;
        LL mask = (1 << (n - 1)) | 1;
        for(int i = 2 | mask; i < (1 << n) && m > 0; i = (i + 1) | mask)
        {
            factors[2] = get_second_factor(i);
            if(factors[2] == i)
                continue;
            int found = 1;
            for(int j = 3; j <= 10; j++)
            {
                LL base = 1;
                LL val = 0;
                for(int k = 0; k < n; k++)
                {
                    val = val + base * ((i >> k) & 1);
                    base = base * j;
                }
                factors[j] = get_second_factor(val);
                if(factors[j] == val)
                {
                    found = 0;
                    break;
                }
            }
            if(found)
            {
                m--;
                for(int j = n - 1; j >= 0; j--)
                    cout << ((i >> j) & 1);
                for(int j = 2; j <= 10; j++)
                    cout << " " << factors[j];
                cout << endl;
            }
        }
        //cout << m << endl;
    }
    return 0;
}
