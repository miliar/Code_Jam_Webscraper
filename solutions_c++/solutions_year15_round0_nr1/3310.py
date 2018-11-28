#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

bool check(int a[], int smax) {
    int cnt = 0;
    for (int i = 0; i <= smax; i++) {
        if (cnt >= i) {
            cnt += a[i];
        } else if (a[i] > 0) {
            return false;
        }
    }
    return true;
}

char buf[1100];
int a[1100];

int main() {    
    int T;
    scanf("%d", &T);
    int smax;    
    for (int t = 1; t <= T; t++) {
        scanf("%d %s\n", &smax, buf);
        for (int i = 0; i <= smax; i++)
            a[i] = buf[i] - '0';
        int ans = 0;
        for (int i = 0; i <= smax; i++) {            
            if (check(a, smax)) {
                ans = i;
                break;
            }
            a[0]++;
        }
        printf("Case #%d: %d\n", t, ans);        
    }
}

