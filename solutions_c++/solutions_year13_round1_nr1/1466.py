#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int work()
{
    long long r, t; cin >>r >> t;
    long long ans = 0;
    long long step = 0;
    while (t > 0)
    {
          if (t >= r + r + step + step + 1)
             ans += 1;
          t -= r + r + step + step + 1;
          step += 2;
    }
    return ans;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >>T;
    for (int t = 1; t <= T; ++ t){
        printf("Case #%d: %d\n", t, work());
    }
    
    return 0;
}
