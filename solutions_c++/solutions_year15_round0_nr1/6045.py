#include<cstdio>
char M[10000];
int main(){
    int cas,t=0;
    freopen("in.txt","r",stdin);

    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    gets(M);
    while(cas--){
        int lvl;
        scanf("%d",&lvl);
        M[0]=getchar();
        gets(M);
        //puts(M);
        int ans=0,aud=0;
        for(int i=0;i<=lvl;i++){
            if(aud<i && M[i]-'0'){
                ans+=(i-aud);
                aud=i;
            }
            aud+=M[i]-'0';
        }
        printf("Case #%d: %d\n",++t,ans);
    }
    return 0;
}
