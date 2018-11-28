#include<stdio.h>
int main(){
    int n;
    int t = 0;
    freopen("jam.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        int m;
        scanf("%d",&m);
        if(m == 0) printf("Case #%d: INSOMNIA\n",i);
        else {
            int check[10];
            for(int k=0;k<10;k++){
                check[k] = 0;
            }
            t = 0 ;
            for(int j=1;j<=80;j++){
                int x = m*j;
                int y = x;
                while(x!=0){
                    check[x%10] = 1;
                    x = x/10;
                }
                int c = 0;
                for(int k=0;k<10;k++){
                    if(check[k] == 0){ c = 1; }
                }
                if(c == 0) { printf("Case #%d: %d\n",i,y); break;}
            }
        }
        
    }
    
}