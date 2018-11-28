#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("B-large.in","r",stdin);
    freopen("outB","w",stdout);
    int T,c=1;
    scanf("%d",&T);
    while(T--){
        char str[1000];
        scanf(" %s",str);
        int len=strlen(str),now=str[0],ans=0,i;
        for(i=0;i<len-1;i++){
            if(str[i+1]!=str[i])ans++;
        }
        printf("Case #%d: %d\n",c++,ans+(str[len-1]=='-'));
    }
    return 0;
}
