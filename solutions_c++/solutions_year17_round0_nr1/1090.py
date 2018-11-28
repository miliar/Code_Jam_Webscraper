#include<bits/stdc++.h>
using namespace std;
char s[1005];
int main(){
    int t,C=0;
    scanf("%d",&t);
    while(t--){
        int k,ans=0,flag=1;
        scanf("%s%d",s,&k);
        int n=strlen(s);
        for(int i=0;i<n-k+1;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=0;j<k;j++){
                    if(s[i+j]=='-') s[i+j]='+';
                    else s[i+j]='-';
                }
            }
        }
        for(int i=0;i<n;i++){
            if(s[i]=='-') flag=0;
        }
        printf("Case #%d: ",++C);
        if(flag) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
}
