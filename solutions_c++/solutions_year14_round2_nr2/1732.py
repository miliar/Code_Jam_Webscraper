#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <utility>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define F first
#define S seccond
#define For(i,n) for (int i = 0; i < n; i++)

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    For(q,t)
    {
            int a, b, c;
            cin >> a >> b >> c;
            int ans = 0;
            For(i,a)
                    For(j,b)
                            if((i & j)<c)ans++;
            cout << "Case #" << q + 1 << ": " << ans << endl;
            }                         
    return 0;
}
