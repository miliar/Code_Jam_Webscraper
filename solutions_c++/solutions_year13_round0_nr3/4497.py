#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;
int t;
int a, b;

bool palin(int n) {
    int p[10];
    int size = 0;
    if(n < 10) return true;
    while(n) {
        p[size++] = n%10;
        n /= 10;
    }
    for(int i = 0; i < size/2; i++) {
        if(p[i] != p[size-i-1]) return false;
    }
    return true;
}
bool check(int n) {
    if(!palin(n)) return false;
    int i = (int)floor(sqrt(n));
    if(i*i == n) return palin(i);
    return false;
}
int main() {
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small.out","w",stdout);
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        
        scanf("%d%d", &a, &b);
        int ans = 0;
        for(int j = a; j <= b; j++) {
            if(check(j)) ans++;
        }
        printf("Case #%d: %d\n",i, ans);
    }
    //system("pause");
    return 0;
}
