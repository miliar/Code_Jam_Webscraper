#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
using namespace std;
#define N 10000
vector<long long> fs;
long long cnt;
bool ispalin(long long n) {
    int a[10], i=0;
    while(n) {
       a[i++] = n % 10; 
       n = n/10;
    }
    i--;
    for (int j=0;j<i;j++,i--) {
        if (a[i] == a[j]) continue;
        else return false;
    }
    return true;
}
int main() {
    int tc;
    scanf("%d", &tc);
    long long limit = sqrt(N);
    for (long long i = 1; i<=limit;i++) {
        if (ispalin(i) && ispalin(i*i)) { 
            fs.push_back(i*i);
//            printf("%d",i);
        }
    }
    long long a,b;
    for(int t=0;t<tc;t++) {
        scanf("%lld %lld", &a, &b);
        long long l= lower_bound(fs.begin(), fs.end(), a)-fs.begin();
        long long h= upper_bound(fs.begin(), fs.end(), b)-fs.begin();
        printf("Case #%d: %lld\n", t+1, h-l);
    }
    return 0;
}
