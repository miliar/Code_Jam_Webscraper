#include<stdio.h>
char str[105][105];
int dx[4] ={-1,0,0,1};
int dy[4] ={0,1,-1,0};
int r,c;
bool good(int i,int j,int k)
{
    i+=dx[k];
    j+=dy[k];
    while(i>=0&&i<r&&j>=0&&j<c){
        if(str[i][j]!='.') return true;
        i+=dx[k];
        j+=dy[k];
    }
    return false;
}
bool nice(int i,int j)
{
    for(int k =0;k<4;k++){
        if(good(i,j,k)) return true;
    }
    return false;
}
int main ()
{
    int T;
    int ans;
    bool ctn = false;
    scanf("%d",&T);
    for(int _ =1;_<=T;_++){
        scanf("%d%d",&r,&c);
        for(int i =0;i<r;i++){
            scanf("%s",str[i]);
        }
        ans =0;
        ctn = true;
        for(int i =0;i<r&&ctn;i++){
            for(int j =0;j<c&&ctn;j++){
                if(str[i][j]=='.') continue;
                if(!nice(i,j)){
                    ctn = false;
                }
                if(str[i][j]=='^'){
                    if(!good(i,j,0)){
                        ans++;
                    }
                }else if(str[i][j]=='>'){
                    if(!good(i,j,1)){
                        ans++;
                    }
                }else if(str[i][j]=='<'){
                    if(!good(i,j,2)){
                        ans++;
                    }
                }else if(str[i][j]=='v'){
                    if(!good(i,j,3)){
                        ans++;
                    }
                }
            }
        }
        if(ctn)
            printf("Case #%d: %d\n",_,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",_);

    }
    return 0;
}