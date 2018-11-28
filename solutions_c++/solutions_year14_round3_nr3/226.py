#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <stack>
#include <cmath>
#include <map>
#include <utility>
#include <set>
#include <algorithm>


using namespace std;

int main ()
{
    ios_base::sync_with_stdio(false);
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);


    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        int n, m ,kk;
        cin >> n >> m >> kk;
        int minVal = kk;
        for (int j = 1; j <= m - 2; ++j)
        {
            for (int k = 1; k <= n - 2; ++k)
            {
                int temp = 2 * k + 2 * j;
                int covered = temp + k * j;
                //cout << temp << " " << covered << endl;
                if ((covered >= kk) && (temp < minVal))
                {
                    minVal = temp;
                }
                else if ((k > 1 || j > 1) && covered - 2 >= kk && temp - 1< minVal)
                    minVal = temp - 1;
                else if ((covered < kk) && (temp + kk - covered < minVal))
                    minVal = temp - covered + kk;

            }
        }
        cout << minVal << endl;

    }
}

