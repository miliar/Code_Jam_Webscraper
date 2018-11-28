#include<stdio.h>
#include<string.h>
int main(){
    int n;
    freopen("jam.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        char a[1001];
        
        scanf("%s",a);
        int m = (int)strlen(a);
        int x = 101;
        int count = 0;
        int check = 0;
        
        for(int j=0;j<m;j++){
            if(a[j] == '-'){ check = 1; x = j;}
        }
        while(check == 1){
            check = 0;
            for(int j=0;j<m;j++){
                if(a[j] == '-'){ check = 1;  x = j;}
            }
            if(check == 1){ count++; }
            for(int j=0;j<=x;j++){
                if(a[j] == '-') { a[j] = '+'; }
                else a[j] ='-';
            }
        }
        printf("Case #%d: %d\n",i,count);
    }
    
}