#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cassert>
#include <cstdio>
using namespace std;



int solve(){
    int k; cin>>k;k++;
    string s;cin>>s;
    assert(s.size() == k);

    int cur = 0;
    int ret = 0;

    for(int i = 0; i < k; i++){
        int num = s[i] - '0';
        if(!num) continue;

        if(cur < i) {
            int s = i - cur;
            ret += s;
            cur += s;
        }

        cur += num;
    }

    return ret;

}


int main() {
    freopen("C:\\a.txt","r",stdin);
    freopen("C:\\w.txt","w",stdout);

    int n;cin>>n;
    for(int i = 1; i <= n;i++){
        printf("Case #%d: %d\n",i,solve());

    }
    return 0;
}
