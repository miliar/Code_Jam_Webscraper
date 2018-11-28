#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int a;

vector <int> ans;

int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0;i < t;i++){
        map <int, int> m;
        int n;
        cin >> n;
        ans.clear();
        for (int j = 0;j < (2 * n - 1) * n;j++){
            cin >> a;
            m[a]++;
        }
        map<int, int>::iterator it;
        for (it = m.begin();it != m.end();it++){
            //cout << it->first << " " << it->second << endl;
            if (it->second & 1){
                ans.push_back(it->first);
            }
        }
        sort(ans.begin(), ans.end());
        printf ("Case #%d: ", i + 1);
        for (int j = 0;j < n;j++){
            printf ("%d ", ans[j]);
        }
        printf ("\n");
    }
    return 0;
}