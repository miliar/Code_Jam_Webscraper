#include<stdio.h>

int i,j,r,c,q,k,ch[110][110],chq,ans;
char t[110][110];

int main(){
    scanf("%d",&q);
    for(k=1;k<=q;k++){
        chq=0;
        ans=0;
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++){
            for(j=0;j<c;j++)ch[i][j]=0;
            scanf("%s",t[i]);
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(t[i][j]!='.'){
                    ch[i][j]++;
                    if(t[i][j]=='<'){
                        ans++;
                    }
                    break;
                }
            }
            for(j=c-1;j>=0;j--){
                if(t[i][j]!='.'){
                    ch[i][j]++;
                    if(t[i][j]=='>'){
                        ans++;
                    }
                    break;
                }
            }
        }
        for(j=0;j<c;j++){
            for(i=0;i<r;i++){
                if(t[i][j]!='.'){
                    ch[i][j]++;
                    if(t[i][j]=='^'){
                        ans++;
                    }
                    break;
                }
            }
            for(i=r-1;i>=0;i--){
                if(t[i][j]!='.'){
                    ch[i][j]++;
                    if(t[i][j]=='v'){
                        ans++;
                    }
                    if(ch[i][j]==4)chq=1;
                    break;
                }
            }
        }
        if(chq==1)printf("Case #%d: IMPOSSIBLE\n",k);
        else printf("Case #%d: %d\n",k,ans);
    }
}
