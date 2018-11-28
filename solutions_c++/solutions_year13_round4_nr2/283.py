#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;
#define ll long long
ll cf[100];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    ll p;
    int i, n, t;
    ll ans1, ans2;
    int ts, ks;
    
    
    cf[0] = 1;
    for (i = 1; i <= 50; i++) cf[i] = cf[i - 1] * 2;
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> n >> p;
        if (p == cf[n]){
           cout << "Case #" << ks + 1 << ": " << cf[n] - 1 << " " << cf[n] - 1 << endl;
           continue;
        }
        //
        ans1 = 0;
        for (i = n - 1; i >= 0; i--) 
            if (((p - 1) & cf[i]) == 0) 
               break;
            else ans1 += cf[n - i];
        
        //
        for (i = n - 1; i >= 0; i--)
            if (p == cf[i]) break;
        if (i >= 0) t = i;
        else {
             for (i = n - 1; i >= 0; i--)
                 if ((p - 1) & cf[i]) break;
             t = i;
        }
        t = n - t;
        ans2 = cf[n] - cf[t];
        
        cout << "Case #" << ks + 1 << ": " << ans1 << " " << ans2 << endl; 
    }
    return 0;
}
