#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>
#include <time.h>
#include <errno.h>
#include <Semaphore.h>

using namespace std;

string fun(int n, int r, int p, int s) {
    if (s+r<p || p+r<s || p+s<r) {
        return "IMPOSSIBLE";
    }
    
    string ret = "";
    if (n == 1) {
        if (p > 0) ret += "P";
        if (r > 0) ret += "R";
        if (s > 0) ret += "S";
        return ret;
    }
    
    int a = (s+r-p)/2;
    int b = (p+r-s)/2;
    int c = (p+s-r)/2;
    
    string tmp = fun(n-1, a, b, c);
    if (tmp == "IMPOSSIBLE") {
        return "IMPOSSIBLE";
    } else {
        for (int i = 0; i < tmp.length(); i++) {
            if (tmp[i] == 'P') {
                ret += "PR";
            } else if (tmp[i] == 'R') {
                ret += "RS";
            } else {
                ret += "PS";
            }
        }
        
        for (int i = 1; i < n; i++) {
            int len = (1 << i);
            int index = 0;
            tmp = ret;
            ret = "";
            while (index < tmp.length()) {
                string a = tmp.substr(index, len);
                string b = tmp.substr(index+len, len);
                if (a > b) {
                    ret += b + a;
                } else {
                    ret += a + b;
                }
                index += len * 2;
            }
        }
        return ret;
    }
}

int main() {
    freopen("/Users/lujcmss/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/a-out.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        
        string ret = fun(n, r, p, s);
        
        printf("Case #%d: %s\n", kase + 1, ret.c_str());
    }
    return 0;
}