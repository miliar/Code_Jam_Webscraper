#include<bits/stdc++.h>
using namespace std;

int t,k,c,s;


int main(){
    freopen("dd.in","r",stdin);
    freopen("d.txt","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        printf("Case #%d: ",ca);
        scanf("%d %d %d",&k,&c,&s);

        for(int i = 1;i<=k;i++){
            if(i>1)printf(" ");
            printf("%d",i);
        }printf("\n");


    }
    return 0;
}
