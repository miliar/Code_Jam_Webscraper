#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

int kasus,banyak;
long long bet[40],uang;

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        cin>>uang>>banyak;
        for (int i=0;i<banyak;++i) cin>>bet[i];
        for (int i=banyak;i<37;++i) bet[i] = 0;
        sort(bet,bet+37);
        
        double jawab = 0.0;
        for (int i=0;i<37;++i) {
            if (i < 36 && bet[i] == bet[i+1]) continue;
            //cout<<i+1<<" : "<<bet[i]<<endl;
            for (int k=i;k>-1;--k) {
                long long total = 0;
                for (int j=0;j<=k;++j) total += (bet[i]-bet[j]);
                long long biaya = total;
                for (int j=k+1;j<=i;++j) biaya += (bet[i]+1LL-bet[j]);
                
                if (biaya > uang) continue;
                long long sisa = uang-biaya;
                long long naik = min(sisa / (long long)(i+1),bet[i+1]-bet[i]-1);
                if (i < 36) {
                    total += naik * (long long)(k+1);
                    biaya += naik * (long long)(i+1);
                }
                double untung = (double)total*(36.0/(double)(k+1)) - (double)biaya;
                
                //cout<<total<<": "<<untung<<" "<<naik<<endl;
                jawab = max(jawab,untung);
            }
        }
        
        printf("Case #%d: %.6lf\n",l,jawab);
    }
    return 0;
}
