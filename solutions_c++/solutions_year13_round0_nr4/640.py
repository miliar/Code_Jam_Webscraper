#include <cstdio>
#include <cstdlib>
#include <cmath>

#define maxn 101

int a[maxn];
int total;
long long n;
long long m;

bool check(long long x) {
    int len = 0;
    long long k = x;
    
    while (k > 0) {
        a[len] = k % 10;
        k = k / 10;
        len++;
    }
    
    for (int i = 0; i < len / 2; i++) 
        if (a[i] != a[len - 1 - i])
            return false;
        
    return true;
}

int main() {
    
    FILE *fi = fopen("C-large-1.in", "r");
    FILE *fo = fopen("output.txt", "w");
    
    fscanf(fi, "%d", &total);
    
    for (int t = 0; t < total; t++) {
        fscanf(fi, "%lld%lld", &n, &m);
        
        long long a = (long long)sqrt(n);
        long long b = (long long)sqrt(m);
        
        long long cnt = 0;
        for (long long i = a; i <= b; i++)
            if (check(i)) {
                long long sq = i * i;
                if (sq >= n && check(sq))
                    cnt++;
            }
                
        fprintf(fo, "Case #%d: %lld\n", t + 1, cnt);
            
    }
    
    fclose(fi);
    fclose(fo);
    
    return 0;
}
