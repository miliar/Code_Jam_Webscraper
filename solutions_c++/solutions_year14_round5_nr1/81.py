#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

long long n, p, q, r, s;
long long cum[1000000];

long long findSearch(int start, int end, long long val) {
    if (start == end)
        return start;
    if (cum[end] < val)
        return end;
    int mid = (start + end)/2;
    if (cum[mid] > val)
        return findSearch(start, mid, val);
    return findSearch(mid+1, end, val);
}


bool possible(long long val) {
    int first = findSearch(0, n, val)-1;
    //printf("finding %lld %lld\n", val, cum[first]);
    int second = findSearch(0, n, cum[first] + val)-1;
    long long final = cum[n] - cum[second];
    
    //printf("possible %lld %d\n", val, final <= val);
    
    return final <= val;
}

long long binsearch(long long start, long long end) {
    if (start == end)
        return start;
    long long mid = (start + end)/2;
    if (possible(mid))
        return binsearch(start, mid);
    return binsearch(mid+1, end);
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%lld %lld %lld %lld %lld", &n, &p, &q, &r, &s);
        long long i;
        long long sum = 0;
        cum[0] = 0;
        for (i = 0; i < n; i++) {
            sum += (i*p + q) % r + s;
            cum[i+1]= sum;
        }
        
        
        printf("%.11lf\n", 1.0-double(binsearch(0, cum[n]))/cum[n]);
        
        
            
    }
}