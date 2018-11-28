#include<stdio.h>
#include<math.h>
int main(){
    freopen("A.in","r",stdin);
    freopen("output.out","w",stdout);
    long i,n,r,t,count,k;
double ml = 0.0,bar = 0.0,area1=0.0,area2 = 0.0;
double pai = acos(-1);
while(scanf("%ld",&n)==1){
    for(i=1;i<=n;i++){
        scanf("%ld %ld",&r,&t);
        ml = t*pai;
        k=r+1;
        count = 0;
        while(1){
            area1 = pai*pow(r,2);
            area2 = pai*pow(k,2);
            bar = area2-area1;
            if(bar<=ml||fabs(bar-ml)<=0.0000001){
                count++;
                ml= ml-bar;
                k+=2;
                r=k-1;
            }else{
                break;
            }
        }
        printf("Case #%ld: %ld\n",i,count);
    }

}
    fclose(stdout);
    fclose(stdin);
return 0;
}
