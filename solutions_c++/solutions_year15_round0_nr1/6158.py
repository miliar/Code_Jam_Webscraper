#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cases=0;
    scanf("%d",&T);
    while(T--){
        int ans=0,N;
        scanf("%d",&N);
        char str[1009];
        scanf("%s",str);
        int total=0;

        for(int i=1;i<=N;i++){
            total=total+(str[i-1]-'0');
            if(total < i) {total++;ans++;}

        }

        printf("Case #%d: %d\n",++cases,ans);
    }
    return 0;
}
