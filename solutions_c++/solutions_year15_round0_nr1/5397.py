#include <stdio.h>
#include <algorithm>
using namespace std;
int shy[1001];
int smax;
int T;
int main (){
    scanf("%d",&T);
    for(int t = 1 ; t <= T ;t++){
        fill(shy,shy+1001,0);
        char in[1002];
        scanf("%d %s",&smax,in);
        for(int i = 0 ; i <= smax ;i++ ){
            shy[i]=in[i]-'0';
        }
        int need=0;
        int sum[1001];
        sum[0]=shy[0];
        for(int i = 1 ; i <= smax; i++){
            sum[i]=sum[i-1]+shy[i];
        }
        for(int i = 1 ; i <= smax ; i++){
            if(sum[i-1]+need<i){
                need=i-sum[i-1];
            }
        }
        printf("Case #%d: %d\n",t,need);
    }

}
