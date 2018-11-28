#include<stdio.h>
int n,i,x,l = 5000,r = 5001;
char a[1010],max2=0,b[10010];
int main(){
    freopen("A.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    scanf("%d",&n);
    for(i = 0; i < n; i++){
        for(x = 0;x < 10000; x++) b[x] = 0;
        max2 = 0,l = 5000,r = 5001;
        scanf("%s",a);
        for(x = 0; a[x]; x++){
            if(a[x] >= max2){
                max2 = a[x];
                b[l--] = a[x];
            }
            else{
                b[r++] = a[x];
            }
        }
        printf("Case #%d: ",i + 1);
        for(x = l + 1; x < r; x++){
            printf("%c",b[x]);
        }
        printf("\n");
    }
}