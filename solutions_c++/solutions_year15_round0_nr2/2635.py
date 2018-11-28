#include <iostream>
#include <algorithm>
#include <queue>
#include <functional>
#include <vector>
using namespace std;


int a[10000];
void solve()
{
    int n;
    int ans = 100000;
    int max_s = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
       cin >> a[i];
       max_s = max(max_s,a[i]);
    }
   sort(a,a+n);
   for (int j = max_s; j; j--)
   {
       auto k = upper_bound(a,a+n,j);
       int r = 0;
       for (int i = k-a; i < n; i++){
           r += (a[i]-1)/j;
           if (r + j > ans) break;
       }
       ans = min(ans,r+j);
   }
   cout << ans << endl;
}

int main()
{
    int cases;
    cin.sync_with_stdio(false);
    cin >> cases;
    for (int i = 1; i <= cases; i++)
    {
        cout << "Case #"<<i<<": ";
        solve();
    }
    return 0;
}
