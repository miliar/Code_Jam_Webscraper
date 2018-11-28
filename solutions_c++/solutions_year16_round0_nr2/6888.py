#include<cstdio>
#include<cstring>
int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, len, last, ans;
    char s[105];
    bool stk[105];
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
        printf("Case #%d: ",cases);
        scanf("%s",s);
        ans=0, last=-1;
        len=strlen(s);
        for(int i=0; i<len; i++){
            if(s[i]=='+') stk[i]=1;
            else stk[i]=0, last=i;
        }
        if(last==-1){printf("0\n"); continue;}
        while(!stk[last]){
            for(int i=1; i<=last; i++){
                if(stk[i]==stk[0]) stk[i]^=1;
                else break;
            }
            stk[0]^=1;
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
