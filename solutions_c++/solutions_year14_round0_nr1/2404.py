#include <bits/stdc++.h>
using namespace std;

//long long mod = 1000000007;
//
//long long mypow(long long a,int b){
//    if(b==0)return 1;
//    long long tmp = mypow(a,b/2);
//    tmp = (tmp*tmp)%mod;
//    return (b&1)? ((tmp*a)%mod):tmp;
//}

int main() {
    int T;
    int A[5][5];
    int B[5][5];
    int r1,r2;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&r1);
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                scanf("%d",&A[i][j]);
            }
        }
        scanf("%d",&r2);
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                scanf("%d",&B[i][j]);
            }
        }
        int card = -1;
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                if(A[r1][i]==B[r2][j]){
                    if(card==-1){
                        card = A[r1][i];
                    }
                    else{
                        card = -2;
                    }
                }
            }
        }
        if(card==-1){
            printf("Case #%d: Volunteer cheated!\n",t);
        }
        else if(card==-2){
            printf("Case #%d: Bad magician!\n",t);
        }
        else{
            printf("Case #%d: %d\n",t,card);
        }
    }
    return 0;
}
