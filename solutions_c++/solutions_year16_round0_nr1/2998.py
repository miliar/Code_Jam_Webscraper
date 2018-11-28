#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
using namespace std;

int a[10];
void g(int sum) {
    while(sum > 0) {
        a[sum % 10] = 1;
        sum /= 10;
    }
}
int f(int x) {
    int sum = 0;
    for (int i = 0;i < 100;i ++) {
        sum += x;
        int cur = sum;
        while(cur > 0) {
            a[cur % 10] = 1;
            cur /= 10;
        }
        int tot = 1;
        for (int j = 0;j <= 9;j ++) {
            tot = tot & a[j];
        }
        if(tot == 1) return sum;
    }
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);	
    int T,n;
    scanf("%d",&T);
    int C = 1;
    while(T --) {
        for (int i = 0;i <= 9;i ++) a[i] = 0;
        scanf("%d",&n);
        if(n == 0) printf("Case #%d: INSOMNIA\n",C++);
        else printf("Case #%d: %d\n",C++,f(n));
    }
}
























































































