#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;


const int MAX = 110;
const int MAX2 = 100100;
const int MAXT = 400;
const int INF = 2e9 + 1000;
const long long INFl = 2e18;
const int MOD = 1000000007;
const double EPS = 1e-10;

int a[10], alen = 0;
int b[10], blen = 0;
bool all[10];

bool plust() {
    if(alen > blen) {
        blen = alen;
    }
    int cat = 0;
    for(int i = 0; i < blen; ++i) {
        b[i] += a[i] + cat;
        cat = b[i] / 10;
        b[i] %= 10;
        all[b[i]] = true;
    }
    if(cat > 0) {
        b[blen] = cat;
        all[b[blen]] = true;
        ++blen;
    }
    
    for(int i = 0; i < 10; ++i) {
        if(!all[i])
            return false;
    }
    return true;
}

int main()
{  
    int T, n;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d", &n);
        printf("Case #%d: ", Ti);
        if(n == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        
        for(int i = 0; i < 10; ++i) {
            a[i] = b[i] = 0;
            all[i] = false;
        }
        alen = blen = 0;
        
        while(n > 0) {
            a[alen] = n % 10;
            n /= 10;
            alen++;
        }
        
        while(!plust());
        
        for(int i = blen - 1; i >= 0; --i) {
            printf("%d", b[i]);
        }
        printf("\n");        
    }
}
