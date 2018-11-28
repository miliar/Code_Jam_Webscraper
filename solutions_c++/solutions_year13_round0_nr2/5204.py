#include <stdio.h>

int arr[104][104];
int cek(int i,int j,int b,int c){
    int ct=0;
    for(int x = 0;x < b;x++){
        if( x==i) continue;
        else if(arr[x][j] > arr[i][j]){
            ct++;
            break;
        }
    }
    for(int y = 0;y < c;y++){
        if( y==j) continue;
        else if(arr[i][y] > arr[i][j]){
            ct++;
            break;
        }
    }
   // printf("%d\n",ct);
    if( ct > 1) return 0;
    else return 1;
}

int main(){
    int a;
    
    freopen("B-large.in","r",stdin);
    freopen("resba.out","w",stdout);
    scanf("%d",&a);
    int b,c;
    for(int i = 1; i <= a;i++){
        scanf("%d %d",&b,&c);
        for(int j = 0; j < b;j++){
            for(int k = 0; k < c;k++){
                scanf("%d",&arr[j][k]);    
            }
        }
        
        
        int state = 1;
        for(int j = 0; j < b; j++){
            for(int k = 0; k < c;k++){
                if(cek(j,k,b,c) == 0){
                    state = 0;
                    //printf("break at : %d %d %d\n",j,k,arr[j][k]);
                    break;
                }
            }
            if(state == 0) break;
        }
        
        printf("Case #%d: ",i);
        if(state) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
