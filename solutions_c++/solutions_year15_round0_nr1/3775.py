#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <bitset>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <functional>
#include <iomanip>
#include <cstdlib>


const int mx=1010;
using namespace std;

int n,t;
string s;
int main(){
//    freopen("data.in","r",stdin);
//    freopen("data.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for(int j = 1 ; j <= t ; j++){
        cin >> n >> s;
        int ans = 0, sum = 0;
        for(int i = 0; i < n + 1; i++){
            int d = s[i] - '0';
            if (sum < i){
                ans += (i - sum);
                sum = i;
            }
            sum += d;
        }
        cout << "Case #" << j << ": " << ans << endl;
    }
    return 0;
}

