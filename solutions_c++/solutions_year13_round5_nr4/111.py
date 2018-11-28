#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int banyak,kasus;
char kata[25];
double dp[25][1<<20];
bool sudah[25][1<<20];

double proses(int bitmask) {
    if (bitmask == (1<<banyak)-1) return 0.0;
    if (sudah[banyak][bitmask]) return dp[banyak][bitmask];
    sudah[banyak][bitmask] = true;
    
    dp[banyak][bitmask] = 0.0;
    for (int i=0;i<banyak;++i) {
        if (bitmask & (1<<i)) continue;
        int newb = bitmask | (1<<i);
        dp[banyak][bitmask] += (proses(newb)+(double)banyak)/ (double)banyak;
        
        int kurang = 1;
        int indeks = i-1;
        if (indeks < 0) indeks = banyak-1;
        while (bitmask & (1<<indeks)) {
            dp[banyak][bitmask] += (proses(newb)+(double)(banyak-kurang)) / (double)banyak;
            --indeks;
            ++kurang;
            if (indeks < 0) indeks = banyak-1;
        }
    }
    
    return dp[banyak][bitmask];
}

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%s",kata);
        banyak = strlen(kata);
        int bitmask = 0;
        for (int i=0;i<banyak;++i) {
            if (kata[i] == 'X') bitmask |= (1<<i);
        }
        
        double jawab = proses(bitmask);
        printf("Case #%d: %.9lf\n",l,jawab);
    }
    return 0;
}
