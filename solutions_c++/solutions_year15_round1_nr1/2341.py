#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <iomanip>
#include <cctype>
#include <map>

using namespace std;


void solve(int t) {
    int n; cin>>n;
    vector<int> v(n);
    for(int i = 0;i < n;i++) {
        cin>>v[i];
    }
    long long a = 0,b = 0;
    for(int i = 0;i < (n - 1);i++) {
        if(v[i] > v[i + 1]) a+=v[i] - v[i + 1];
    }
    long long c = v[0];
    long long bmin = 100000000000000000LL;
    for(int j = 0;j <= 10000;j++) {
        b = 0;
        c = v[0];
        int flag = 0;
        for(int i = 1;i < n;i++) {
            if(c >= j) c-=j,b+=j;
            else b+=c,c = 0;
            if(c > v[i]) {
                flag = 1;
                break;
            }
            c = v[i];
        }
        if(!flag) bmin = min(b,bmin);
    }
    printf("Case #%d: %lld %lld\n",t,a,bmin);
}

int main() {
    freopen("/Users/administrator/Desktop/A-large.in","r",stdin);
    freopen("/Users/administrator/Desktop/gcjoutput.txt","w",stdout);
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        solve(i);
    }
}