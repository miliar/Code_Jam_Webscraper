#include<bits/stdc++.h>
using namespace std;
int main(){
    int i,turn,a,b,c;
    scanf("%d",&turn);
    for(i=1;i<=turn;i++){
        scanf("%d %d %d",&a,&b,&c);
        int maxi=max(b,c);
        int mini=min(b,c);
        printf("Case #%d: ",i);
        if(a==1)
            printf("GABRIEL\n");
        else if((a==2)&&((b*c)%2==0)){
            printf("GABRIEL\n");
        }
        else if((a == 3) && (b*c)%3 == 0 && (b>1 && c>1)){
            printf("GABRIEL\n");
        }
        else if((a == 4) && (b*c)%4 == 0 && maxi >= 4 && mini >= 3){
            printf("GABRIEL\n");
        }
        else{
            printf("RICHARD\n");
        }
    }
}
