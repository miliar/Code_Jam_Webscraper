#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string.h>
#include<vector>
#include<cmath>
#include<limits.h>
#define MOD 1000000009
#define MAX 1005

using namespace std;

int main(){

    int test,num,arr[4][4],brr[4][4];
    scanf("%d",&test);
    int c=1;
    while(c<=test){
        int ans1,ans2;
        scanf("%d",&ans1);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&arr[i][j]);
            }
        }
        scanf("%d",&ans2);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&brr[i][j]);
            }
        }

        int res = 0;
        int count = 0;
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                if(arr[ans1-1][i]==brr[ans2-1][j]){
                    res = arr[ans1-1][i];
                    count++;
                    break;
                }
            }
        }
        if(count==1){
            printf("Case #%d: %d\n",c,res);
        }
        else if(count>1){
            printf("Case #%d: Bad magician!\n",c);
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",c);
        }
        c++;
    }
    return 0;

}
