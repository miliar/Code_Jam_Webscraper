#include <bits/stdc++.h>
using namespace std;
int T;
char cake[105],temp[105];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out large.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",cake);
        int len = strlen(cake);
        for(int i=0;i<len;i++){
            if(cake[i]=='-'){
                cake[i] = 0;
            }else{
                cake[i] = 1;
            }
        }
        int counter = 0;
        for(int i=len-1;i>=0;i--){
            if(cake[i]==1)continue;
            if(cake[0]==0){
                for(int j=0;j<=i;j++){
                    temp[i-j] = !cake[j];
                }
                for(int j=0;j<=i;j++){
                    cake[j] = temp[j];
                }
                counter++;
            }else{
                for(int j=0;j<i;j++){
                    if(cake[j]==0){
                        break;
                    }
                    cake[j]=!cake[j];
                }
                for(int j=0;j<=i;j++){
                    temp[i-j] = !cake[j];
                }
                for(int j=0;j<=i;j++){
                    cake[j] = temp[j];
                }
                counter+=2;
            }
        }
        printf("Case #%d: %d\n",t,counter);
    }
    return 0;
}
