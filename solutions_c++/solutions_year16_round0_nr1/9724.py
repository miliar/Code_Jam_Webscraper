#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;
const int all = 1023;
char s[55];
int getVal(long long n) {
    sprintf(s, "%lld", n);
    int len = strlen(s);
    int sum = 0;
    for (int i = 0; i < len; ++i){
        sum |= 1<<(s[i] - '0');
    }
    return sum;
}
long long solve(long long t){
    return all;
}
int main(void) {
    freopen("A-large (1).in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    //printf("1000\n");
    //for (int i = 1000; i < 2000; i++) {
    //    printf("%d\n", i);
    //}
    //return 0;
    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i) {
        long long t;
        scanf("%lld", &t);
        int cur = 0;
        long long tmp = t;
        long long last = -1;
        for(int j=1;j<100000;j++) {
            cur |= getVal(tmp);
            if (cur == all) {
                last = tmp;
                break;
            }
            tmp += t;
            //printf("tmp=%lld\n", tmp);
        }
        if (last == -1) {
            printf("Case #%d: INSOMNIA\n", i+1);
        } else {
            printf("Case #%d: %lld\n", i+1, last);
        }
    }
}
