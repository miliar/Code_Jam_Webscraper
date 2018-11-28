#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }


#define N 1000000
long long a[N];
int an;

int check(long long x){
    long long a = 1, b = 1;
    while (b*10 <= x) b *= 10;

    while (a < b){
        long long t1 = x / a % 10;
        long long t2 = x / b % 10;
        if (t1 != t2) return 0;
        a *= 10; 
        b /= 10;
    }
    
    return 1;
}

int main(){
    an = 0;
    int n = N * 10;
    for (long long i=1;i<n;i++){
        if (check(i) && check(i*i)){
            a[an++] = i*i;
            //printf("%lld %lld\n", i, i*i);
        }
    }
    //printf("%d\n", an);

    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        long long x, y;
        scanf("%lld%lld", &x, &y);
        
        int px = lower_bound(a, a+an, x) - a;
        int py = upper_bound(a, a+an, y) -a ;
        //printf("~ %d(%lld) %d(%lld)\n", px, a[px], py, a[py]);
        int ans=  py - px;
        printf("Case #%d: %d\n",ti,ans);
    }
    
    return 0;
}

