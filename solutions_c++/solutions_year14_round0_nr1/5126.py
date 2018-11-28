#include<bits/stdc++.h>
using namespace std;
int main(){
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        int a1;
        int ar[17];
        memset(ar,0,sizeof(ar));
        scanf("%d",&a1);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(i==(a1-1)){
                    int d;
                    scanf("%d",&d);
                    ar[d]=1;
                }
                else{
                    int d;
                    scanf("%d",&d);
                }
            }
        }
        int a2;
        scanf("%d",&a2);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(i==(a2-1)){
                    int d;
                    scanf("%d",&d);
                    ar[d]++;
                }
                else{
                    int d;
                    scanf("%d",&d);
                }
            }
        }
        int ct1=0;
        for(int i=1;i<=16;i++){
            if(ar[i]==2){
                ct1++;
            }
        }
        if(ct1==1){
            for(int i=1;i<=16;i++){
                if(ar[i]==2){
                    printf("Case #%d: %d\n",t,i);
                    break;
                }
            }
        }
        else if(ct1>1){
            printf("Case #%d: Bad magician!\n",t);
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",t);
        }
    }
    return 0;
}
