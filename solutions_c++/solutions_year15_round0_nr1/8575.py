#include<iostream>
#include<cstdio>
using namespace std;
int main(){
int T;
scanf("%d",&T);
for(int t=1;t<=T;t++){
    int n;
    scanf("%d",&n);
    getchar();
    long int standing=0,required=0;

    for(int i=0;i<=n;i++){
        int cnt=getchar()-'0';

        if(cnt>0&&standing<i){
            required+=i-standing;
            standing=i;

        }
        standing+=cnt;

    }
    getchar();
    printf("Case #%d: %ld\n",t,required);
}
return 0;
}
