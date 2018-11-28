#include <cstdio>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
#include <queue>

using namespace std;
int n, a[1010], res;

bool cmp(int x, int y){return x > y;}

void work(int x){
    int tmp = 0;
    for (int i = 1; i <= n; i++)
        if (a[i] > x) tmp += (int)((a[i] - 1) / x);
    tmp += x;
    if (tmp < res) res = tmp;
    /*int b[1010], m = 0;
    for (int i = n; i > 0; i--)
        if (a[i] > x) b[++m] = a[i];
        else break;
    for (int i = 1; i <= m; i++)
    {
        if (b[i] <= x - i) return 1;
        if (i > x) return 0;
        b[++m] = b[i] - (x - i);
        sort(b + i + 1, b + m, cmp);
        for (int j = i + 1; j <= m; j++) b[j]--;
    }*/
    return;
}

int main(){
    FILE* FIN;
    FILE* FOUT;
    FIN = fopen("/Users/Djy/Documents/4test/B-large.in", "r");
    FOUT = fopen("/Users/Djy/Documents/4test/B-large.out", "w");
    
    
    int T;
    fscanf(FIN, "%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        
        fscanf(FIN, "%d", &n);
        for (int i = 1; i <= n; i++)
            fscanf(FIN, "%d", &a[i]);
        sort(a + 1, a + n + 1, cmp);
        res = a[1];
        
        for (int i = 1; i <= res; i++)
            work(i);
        
        /*int l = 0, r = a[n];
        int res;
        while (l + 1 < r) {
            int mid = (l + r) >> 1;
            if (ck(mid)) r = mid;
            else l = mid;
        }
        
        if (ck(l)) res = l;
        else res = l + 1;*/
        
        fprintf(FOUT, "Case #%d: %d\n", cas, res);
    }
    return 0;
}