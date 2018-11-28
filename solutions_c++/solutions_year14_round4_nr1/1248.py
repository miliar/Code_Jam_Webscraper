#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <map>
#include <ctime>

using namespace std;

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.in", "w", stdout);
#endif
    int T, n, c, x, t = 1;
    
    cin >> T;
    
    while(T--){
        cin >> n >> c;
        vector< int > v;
        for(int i = 0; i < n; i++){
            cin >> x;
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        int tot = 0;
        int i = 0, j = n - 1;
        while(i < j){
            if(v[i] + v[j] <= c){
                ++tot;
                ++i, --j;
            }else{
                ++tot;
                --j;
            }
        }
        if(i == j) {
            ++tot;
        }
        cout << "Case #" << t++ << ": " << tot << endl;
    }
    
    return 0;
}
