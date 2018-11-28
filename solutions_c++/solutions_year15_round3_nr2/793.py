#pragma comment (linker, "/STACK:128000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007

using namespace std;

int fact (int n) {
    int res = 1;
    
    while(n) {
        res *= n;
        n--;
    }
    
    return res;
}

int occur(string alpha, string target) {
    int res =0;
    size_t pos = 0;
    
    while ((pos = alpha.find(target, pos)) != -1) {
        pos++;
        res++;
    }
    
    if (res == 1) {
        res = res;
    }
    
    return res;
}

string getNext (string s, string alpha, int a[]) {
    int k = (int)alpha.length();
    int i = (int)s.length() - 1;
    
    while (i > -1 && a[i] == k-1) i--;
    
    if (i == -1) {
        return s;
    }
    
    a[i]++;
    s[i] = alpha[a[i]];
    i++;
    for (; i < s.length(); i++) {
        a[i] = 0;
        s[i] = alpha[0];
    }
    
    return s;
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    
    int tc; cin >> tc;
    for ( int _ = 0; _ < tc; _++ ) {
        int k, l, s;
        string alpha, target;

        cin >> k >> l >> s;
        cin >> alpha >> target;
        
        int cnt[300]={0};
        double p[300];
        
        for (int i = 0; i < alpha.length(); i++) {
            cnt[alpha[i]]++;
        }

        for (int i = 0; i < alpha.length(); i++) {
            p[alpha[i]] = 1.0L * cnt[alpha[i]] / k;
        }
        
        map<string, int> x;

        int done[101] = {0};
        
        int a[101] = {0};
        string xxx = "";
        for (int i = 0; i < s; i++) xxx += alpha[0];
        int total = 1LL;
        for (int i = 0; i < s; i++) {
            total *= 1LL * k;
        }
        
        for (int i = 0; i < total; i++) {
            done[occur(xxx, target)]++;
            xxx = getNext(xxx, alpha, a);
        }
        
        int poww = 1LL;
        for (int i = 0; i < s; i++) poww *= 1LL * k;

        double res = 0;
        int mmax = 0;
        for ( int i = 1; i < 10; i++ ) {
            res += 1.0L * i * done[i]  / poww;
            mmax = max(mmax, done[i] ? i : 0);
        }
        
        printf( "Case #%d: %.7f\n", _+1, mmax - res );
    }
    
    return 0;
}