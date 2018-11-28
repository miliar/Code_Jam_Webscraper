#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int,int> pii;

pii a[1000];
int rev[1000];

int main()
{
    int t; cin >> t;
    for (int T = 1; T <= t; T++)
    {
        int n; cin >> n;
        vector<pii> v;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i].first;
            a[i].second = i;
            rev[i] = a[i].first;
            v.push_back(a[i]);
        }
        sort(a, a+n);
        int s = 0, l = 0, r = 0;
        for (int i = 0; i < n-1; i++)
        {
            // find ith smallest value - this is a[i]
            // find index of it in v
            int ind = 0;
            while (v[ind].first != a[i].first)
                ind++;
            // distance to left: ind-l
            // distance to right: n-ind-1-r
            if (ind-l < n-ind-1-r)
            {
                for (int j = ind; j > l; j--)
                {
                    swap(v[j], v[j-1]);
                    s++;
                }
                l++;
            }
            else
            {
                for (int j = ind; j < n-1-r; j++)
                {
                    swap(v[j], v[j+1]);
                    s++;
                }
                r++;
            }
        }
        cout << "Case #" << T << ": " << s << "\n";
    }
    return 0;
}