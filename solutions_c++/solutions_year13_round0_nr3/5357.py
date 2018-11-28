#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int isPalindrome(int n){
    int a[100],i=0,j;
    while(n>0){
        a[i++]=n%10;
        n/=10;
    }
    i--;
    for(j=0;j<=i;j++){
        if(a[j]!=a[i-j]){
            return 0;
        }
    }
    return 1;
}
int main(){
    FILE *pt = fopen("outFairSquare.txt","a");
    int high = 1000,i,j=0, square,a,b,t,k;
    int sq = sqrt(high);
    int count;
    int c[sq];
    for(i=1;i<=sq;i++){
        square = i*i;
        if(isPalindrome(i)&&isPalindrome(square)){
            c[j++]=square;
        }
    }
    scanf("%d",&t);
    for(i=1;i<=t;i++){
            count=0;
        scanf("%d %d",&a,&b);
        for(k=0;k<j;k++){
            if(c[k]>=a&&c[k]<=b){
                count++;
            }
            if(c[k]>b)
                break;
        }
        fprintf(pt,"Case #%d: %d\n",i,count);
        printf("Case #%d: %d\n",i,count);

    }

    fclose(pt);
}
