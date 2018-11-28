#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <map>

#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;
const int INF = (1<<30);

int memo[101][2];

int doit(int len, int face) {
    if(len == 1) {
        return !face;
    }
    
    int &ret = memo[len][face];
    if(ret != -1) return ret;
    
    ret = INF;
    
    int odd = len % 2;
    if(face) {
        if(odd) {
            //end with 1
            ret = min(ret, doit(len - 1, face));
        }else {
            //ends with 0
            //make everything prefixed with 1 and flip those
            //make everythign 1
            ret = min(ret, doit(len - 1, face) + 2);
        }
    }else {
        if(odd) {
            ret = min(ret, doit(len, !face) + 1);
            ret = min(ret, doit(len - 1, face) + 2);
        }else {
            ret = min(ret, doit(len-1, face));
        }
    }
    
    return ret;
    
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-output", "w", stdout);
    
    memset(memo, -1, sizeof(memo));
    
    int T;
    cin>>T;
    for(int tc = 1; tc <= T; tc++) {
        cout<<"Case #"<<tc<<": ";
        string panc;
        cin>>panc;
        int len = 1;
        for(int i = 1; i < panc.size(); i++) {
            if(panc[i] != panc[i-1]) {
                len++;
            }
        }
        cout<<doit(len, panc[0]=='+')<<endl;
    }
    return 0;
}
