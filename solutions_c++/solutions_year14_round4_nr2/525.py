#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

bool sudah[1005][1005];
int dp[1005][1005],toright[1005],toleft[1005],banyak,ubah[1005],kasus;
pair<int,int> isi[1005];

int proses(int kiri,int kanan) {
    if (kiri == kanan) return 0;
    if (sudah[kiri][kanan]) return dp[kiri][kanan];
    int cur = banyak-(kanan-kiri+1)+1;
    sudah[kiri][kanan] = true;
    dp[kiri][kanan] = min(proses(kiri+1,kanan)+toleft[cur],proses(kiri,kanan-1)+toright[cur]);
    return dp[kiri][kanan];
}

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d",&banyak);
        for (int i=1;i<=banyak;++i) {
            scanf("%d",&isi[i].first);
            isi[i].second = i;
        }
        sort(isi+1,isi+banyak+1);
        
        for (int i=1;i<=banyak;++i) ubah[isi[i].second] = i;
        
        for (int i=1;i<=banyak;++i) {
            toleft[ubah[i]] = 0;
            toright[ubah[i]] = 0;
            for (int j=i-1;j>0;--j) if (ubah[j] > ubah[i]) ++toleft[ubah[i]];
            for (int j=i+1;j<=banyak;++j) if (ubah[j] > ubah[i]) ++toright[ubah[i]];
        }
        
        memset(sudah,0,sizeof(sudah));
        printf("Case #%d: %d\n",l,proses(1,banyak));
    }
    return 0;
}