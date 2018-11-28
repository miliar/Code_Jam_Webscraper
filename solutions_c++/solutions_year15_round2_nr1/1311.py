/**
 * Md Imran Hasan Hira (imranhasanhira@gmail.com)
 */

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int rev(int n){
    int r=0;
    while(n){
        r = r*10 + n%10;
        n = n/10;
    }
    return r;
}

int main(){

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("aout.txt", "w", stdout);

    int T,n;

    cin >> T;
    for(int test=1;test<=T;test++){
        cin >> n;
        vector<int> v(n+1, 99999999);
        v[1] = 1;
        for(int i=2;i<=n;i++){
            v[i] = min(v[i] , v[i-1]+1);
            int r = rev(i);
            if(r > i && r <= n ) v[r] = min(v[r] , v[i]+1);
        }

        //for(int i=0;i<=n;i++) cout << i << " " << v[i] << endl;

        printf("Case #%d: %d\n", test, v[n]);
    }
    return 0;
}
