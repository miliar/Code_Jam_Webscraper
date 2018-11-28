#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

int kasus,maks,n,isi[10005];

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d %d",&n,&maks);
        for (int i=0;i<n;++i) scanf("%d",&isi[i]);
        sort(isi,isi+n);
        
        int jawab = n;
        int indeks = n-1;
        for (int i=0;i<n && i < indeks;++i) {
            while (isi[i] + isi[indeks] > maks && i < indeks) --indeks;
            if (i < indeks) {
                --indeks;
                --jawab;
            }
        }
        
        printf("Case #%d: %d\n",l,jawab);
    }
    return 0;
}
