#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

char m[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        // 何回ファクトリーを買うか決める
        double cps = 2;
        double past = 0;
        double ans = past + x / cps;
        while(true){
            past += c / cps;
            cps = cps += f;
            double da = past + x / cps;
            if(da > ans){ break; }
            ans = da;
        }
        printf("Case #%d: ",r+1);
        printf("%.7lf",ans);
        printf("\n");
    }

}
