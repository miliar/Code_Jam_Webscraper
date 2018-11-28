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
#include <cassert>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d:", i + 1);
        int n;
        cin >> n;
        vector<int> data(n);

        for (int j = 0; j < n; j++)
        {
            int tmp;
            cin >> tmp;
            data[j] = tmp;
        }
        while (1)
        {
            int maxx = 0;
            int next = 0;
            vector<int> dat;
            for (int j = 0; j < n; j++)
            {
                if (maxx < data[j])
                {
                    next = maxx;
                    maxx = data[j];
                    dat = { j };
                }
                else if (maxx == data[j])
                    dat.push_back(j);
                else if (data[j] > next)
                    next = data[j];
            }
            if (maxx == 0)
                break;
            for (int j = 0; j < (maxx - next); j++)
            {
                if (dat.size() % 2 == 0)
                
                    for (int k = 0; k < dat.size(); k += 2)
                    {
                        cout << " " << (char)(dat[k] + 'A') << (char)(dat[k + 1] + 'A');
                        data[dat[k]]--, data[dat[k+1]]--;
                    }
                else
                {
                    cout << " " << (char)(dat[0] + 'A');
                    data[dat[0]]--;
                    for (int k = 1; k + 1 < dat.size(); k += 2)
                    {
                        cout << " " << (char)(dat[k] + 'A') << (char)(dat[k + 1] + 'A');
                        data[dat[k]]--, data[dat[k+1]]--;

                    }
                }

            }

        }
        cout << endl;


    }
    return 0;
}