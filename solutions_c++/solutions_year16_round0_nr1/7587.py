//
// Created by 金宇超 on 16/4/9.
//

#include <iostream>
/*
5
0
1
2
11
1692

1 ≤ T ≤ 100.
Small dataset 0 ≤ N ≤ 200
Large dataset 0 ≤ N ≤ 10^6

Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076

 */
int main() {
    int T;
    FILE* f=fopen("./A-large.in","r");
    FILE* o=fopen("./small.out","w");
    fscanf(f,"%d\n",&T);//T=1
    int cnt[10]={0};
    int cntt=0;
    for(int i=0; i<T; i++) {
        int n;
        cntt=0;
        memset(cnt, 0, sizeof(int)*10);
        fscanf(f, "%d", &n);
        if(n==0) {
            printf("Case #%d: INSOMNIA\n",i+1);
            continue;
        }
        int tn;
        int j;
        for(j=1; j<1000; j++) {
            tn=n*j;
            while(tn>0) {
                int r=tn%10;
                cntt+=cnt[r]==0?1:0;
                cnt[r]=1;
                tn=tn/10;
            }
            if(cntt==10){
                break;
            }
        }
        if(cntt==10) {
            fprintf(o,"Case #%d: %d\n",i+1, n*j);
        } else {
            fprintf(o,"Case #%d: INSOMNIA\n",i+1);
        }
    }
}