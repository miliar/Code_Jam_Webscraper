#include <stdio.h>
#include <math.h>
int palindrome(int n){
    int temp=n;
    int sum=0;
    
    while(temp){
     int r=temp%10;
     temp=temp/10;
     sum=sum*10+r;
    }
    if(n == sum)return 1;
    else return 0;
}
int main(){
    int a;
    int b,c;
    float d;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("resc.out","w",stdout);
    scanf("%d",&a);
    for(int i = 0; i < a;i++){
        int ct = 0;
        scanf("%d %d",&b,&c);
        for(int j = b;j <= c;j++){
            d = sqrt(j);
            int x = (int) d*d;
            //printf("%d %d %d %d\n",x,j,palindrome(j),palindrome(d));
            if(x == j && palindrome(j) && palindrome(d))ct++;
        }
        printf("Case #%d: %d\n",i+1,ct);
    }
}
