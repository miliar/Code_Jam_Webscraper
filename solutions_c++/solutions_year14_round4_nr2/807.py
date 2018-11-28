#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

int a[10010];
int tmp[10010];
int n;

int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    ios::sync_with_stdio();
    int t;
    cin >> t;
    for(int tt = 1 ; tt <= t ; ++tt)
    {
        cin >> n;
        for(int i = 0 ; i < n ; ++i)
            cin >> a[i];
        
        int ans = 0;
        
        for(int i = 0 ; i < n ; ++i)
        {
            int c1, c2;
            c1 = c2 = 0;
            for(int j = 0 ; j < i ; ++j)
            if(a[i] < a[j])
                ++c1;
            for(int j = i+1 ; j < n ; ++j)
            if(a[i] < a[j])
                ++c2;
            
            ans += min(c1, c2);
        }
        
        cout << "Case #" << tt << ": " << ans << "\n";
    }
    return 0;
}