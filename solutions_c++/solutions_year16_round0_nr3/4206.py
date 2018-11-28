#include<cstdio>
#include<cmath>
#include<map>
#include<vector>
using namespace std;
long long base_cal(long long num,long long base){
    long long sum=0,sum_base=1,bmask=1;
    while(num > 0){
        sum=sum+(sum_base*(num & bmask));
        sum_base*=base;
        num = num >> 1;
        //printf("%d %d\n",num,sum);
    }
    return sum;
}
long long check_prime(long long num){
    long long sqr = sqrt(num);
    if(num==1)return num;
    for(long long i=2;i<=sqr;i++){
        if(num%i==0) return i;
    }
    return 0;
}
int main(){
    int T;

    long long ans[20],div_ans[20];
    long long N,J,start_num,end_num;
    scanf("%d",&T);
    scanf("%lld %lld",&N,&J);
    start_num = (long long)pow(2,N-1) + 1;
    end_num = (long long)pow(2,N) - 1;
    printf("Case #1:\n");
    for(long long i=start_num;i<=end_num;i+=2){
        int chk=0;
        for(int j=2;j<=10;j++){
            ans[j]=base_cal(i,j);
            div_ans[j]=check_prime(ans[j]);
            if(div_ans[j]==0){
                chk=1;
                break;
            }
        }
        if(chk==0){
            J--;
            printf("%lld ",ans[10]);
            for(int j=2;j<=10;j++)
                printf("%lld ",div_ans[j]);
            printf("\n");
            if(J==0)break;
        }
    }
    return 0;
}
