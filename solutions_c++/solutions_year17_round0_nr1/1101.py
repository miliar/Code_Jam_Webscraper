#include<stdio.h>
#include<string.h>
char s[10000];
int k;
void doit(){
    scanf("%s%d",s,&k);
    int ans=0;
    int n = strlen(s);
    for(int i=0;i<=n-k;i++){
        if(s[i] == '-'){
            for(int j=0;j<k;j++){
                if(s[i+j] == '-'){
                    s[i+j] = '+';
                }else{
                    s[i+j] = '-';
                }
            }
            ans++;
        }
    }
    for(int i=n-k;i<n;i++){
        if(s[i] == '-'){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%d\n",ans);
}
int main(){
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        doit();
    }
}
