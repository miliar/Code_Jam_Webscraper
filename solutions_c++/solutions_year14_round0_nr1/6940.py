#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int arr[16];
int main(){

    int t, i, j, n, m, p, count, num = -1;

    scanf("%d",&t);

    for(j = 1; j<t; j++){

        num = -1;
        count = 0;
        memset(arr, 0, sizeof(arr));
        scanf("%d ", &n);
        for(i = 0;i<16; i++){
            scanf("%d",&p);
            if(i>=4*(n-1)&&i<4*n){
                arr[p] = 1;
            }
        }
        scanf("%d ", &m);
        for(i = 0;i<16; i++){
            scanf("%d",&p);
            if(i>=4*(m-1)&&i<4*m){
                if(arr[p]==1){
                    count++;
                    num = p;
                }
            }
        }
        if(count==1)
            printf("Case #%d: %d\n", j, num);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",j);
        else
            printf("Case #%d: Bad magician!\n",j);
    }
}
