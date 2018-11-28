#include<iostream>
#include<set>
#include<algorithm>
#include<vector>
#include<queue>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int arr[100],n;
void make_arr(int m){
    int i;
    for(i=0;i<n;i++){
        arr[i] = m%2;
        m/=2;
    }
}
int main (){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T,m,p;
    int ca = 0;
    int big,small,j;
    int ans1=0,ans2=0,ok;
    int i,k,tmp;
    int cnt;
    scanf("%d",&T);
    while(T--){
        ca++;
        printf("Case #%d: ",ca);
        scanf("%d%d",&n,&p);
        memset(arr,0,sizeof(arr));

        //for(i=0;i<n;i++)printf("%d",arr[i]);
        //printf("\n");
        for(i=0;i<(1<<n);i++){
            small = i;
            big = (1 << n) - i - 1;
            tmp = 0;
            cnt = 0;
            while(small > 0){
                small = (small-1)/2;
                tmp = tmp * 2 + 1;
                cnt++;
            }
            for(j=cnt;j<n;j++)tmp = tmp * 2;
            //printf("tmp %d\n",tmp);
            if(tmp < p)ans1 = i;
        }

        for(i=0;i < (1 << n) ;i++){
            for(k=0;k<p;k++){
                make_arr(k);
                small = i;
                big = (1 << n) - i - 1;
                //printf("i %d small %d big %d\n",i,small,big);
                ok = 1;
                for(j=n-1;j>=0;j--){
                    if(arr[j] == 0){
                        if(big == 0)ok = 0;
                        big = (big-1)/2;
                    }else{
                        if(small == 0)ok = 0;
                        small = (small-1)/2;
                    }
                }
                if(ok == 1){
                    ans2 = i;
                }
            }
        }
        printf("%d %d\n",ans1,ans2);
    }
    return 0;
}
