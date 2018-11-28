#include<cstdio>
#include<cstring>
int main(){

    freopen("output.out","w+",stdout);
    int t,n,ans,len;
    char s[1004];
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        memset(s,0,sizeof(s));
        ans=0;
        scanf("%s %d",s,&n);
        len=(int)strlen(s);
        for(int j=0;j<=len-n;j++){
            if(s[j]=='-'){
                ans++;
                for(int k=j;k<j+n;k++){
                    if(s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                }
            }
        }
        for(int j=len-1;j>=len-n;j--){
            if(s[j]=='-'){
                ans=-1;
                printf("Case #%d: IMPOSSIBLE\n",i);
                break;
            }
        }
        if(ans!=-1)
            printf("Case #%d: %d\n",i,ans);
    }
}
