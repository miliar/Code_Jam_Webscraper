#include<cstdio>
int main(){
    int test;
    double C,F,X,a[100019],P=2.0,ans;
    scanf("%d",&test);
    for(int tc=0;tc<test;tc++){
        scanf("%lf%lf%lf",&C,&F,&X);
        a[0] = 0;
        for(int i=1;i<int(X+10);i++) a[i] = a[i-1] + C/(P + double(i-1)*F);
        a[0] = X/P;
        ans =a[0];
        for(int i=1;i<int(X+10);i++){
            a[i] += X/(P + double(i)*F);
            if(a[i] > a[i-1]){
                 ans = a[i-1];
                 break;
            }
        }
        printf("Case #%d: %.7lf\n",tc+1,ans);
    }
}


