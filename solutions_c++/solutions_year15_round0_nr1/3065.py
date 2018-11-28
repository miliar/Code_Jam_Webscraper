#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,j;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        int n,c=0,i,sum=0;
        scanf("%d",&n);
        char inp[n+1];
        scanf("%s",inp);
        for(i=0;i<=n;i++){
               if(i>sum){
                c+=i-sum;
                sum=sum+(i-sum)+(inp[i]-'0');
               // printf("%d\n",i);
               }
            else
         sum=sum+(inp[i]-'0');
        }


        printf("Case #%d: %d\n",j,c);
    }
    return 0;
}
