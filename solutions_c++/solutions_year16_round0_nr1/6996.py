
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <algorithm>
#include <map>
#include <streambuf>
#include <sstream>
#include <queue>
#include <iomanip>
#define ll long long
#define INF 1e9
#define PI acos(-1.0)



using namespace std;

bool all(vector<bool> v) {
int n = v.size();
for(int i = 0; i < v.size(); i++)
    if(!v[i])
    return 0;
return 1;
}

int main() {
freopen("A-large.in","r",stdin);
freopen("output.out","w",stdout);
int T;
scanf("%d",&T);
for(int t = 1 ; t <= T; t++) {
    ll z;
    scanf("%lld",&z);
    if(z == 0) {
         printf("Case #%d: INSOMNIA\n",t);
         continue;
    }
    vector<bool> mp;
    for(int i = 0; i < 10; i++)
        mp.push_back(0);
    ll f = z;
    ll i = 1;
    while(!all(mp)) {
        ll x = i * z;
        f = x;
        while(f > 0) {
            int rem = f % 10;
            mp[rem] = 1;
            f /= 10;
        }
        i++;
    }
    printf("Case #%d: %lld\n",t,(i-1)*z);

}
  return 0;
}

