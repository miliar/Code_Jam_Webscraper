#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 1001
#define ll long long

using namespace std;

int t, n;
string str;

int main(void){
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> n >> str;
        ll ans = 0, up = str[0] - '0';
        for(int i = 1; i < str.size(); i++){
            if(up < i){
                ans += i - up;
                up += i - up;
            }
            up += str[i] - '0';
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}
