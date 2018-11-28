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

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("alout.txt", "w", stdout);
    int T, n;
    string s;
    cin >> T;
    for(int test=0;test<T;test++){
        cin >> n >> s;
        LL res=0, sum=0;
        for(int i=0;i<s.size();i++){
            if( sum+res < i) res += i - (sum+res);
            sum += s[i] - '0';
        }
        printf("Case #%d: %ld\n", test+1, res);
    }

    return 0;
}
