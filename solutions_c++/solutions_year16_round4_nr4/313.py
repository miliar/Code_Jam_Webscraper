#include<bits/stdc++.h>
using namespace std;
int n;
char s[10][10];
int p[10];
bool debug=0;
bool dfs(int cur,int mask){
    if(cur>=n)return 1;
    int u=p[cur];
    bool flag=0;
    for(int i=0;i<n;i++){
        if(mask>>i&1)continue;
        if(s[u][i]=='0')continue;
        if(dfs(cur+1,mask|(1<<i)))flag=1;
        else return 0;
    }
    return flag;
}
bool check1(){
    for(int i=0;i<n;i++)p[i]=i;
    do{
        if(!dfs(0,0))return 0;
    }while(next_permutation(p,p+n));
    return 1;
}
void solve(){
    scanf("%d",&n);    
    for(int i=0;i<n;i++)scanf("%s",s[i]);
    int ans=n*n+1;
    for(int mask=0;mask<1<<(n*n);mask++){
        bool flag=1;
        int cnt=0;
        for(int j=0;j<n&&flag;j++){
            for(int k=0;k<n&&flag;k++){
                int tmp=j*n+k;
                if(mask>>tmp&1){
                    cnt++;
                    if(s[j][k]=='1'){
                        flag=0;
                        break;
                    }
                }
            }
        }
        if(!flag)continue;
        for(int j=0;j<n&&flag;j++){
            for(int k=0;k<n&&flag;k++){
                int tmp=j*n+k;
                if(mask>>tmp&1){
                    s[j][k]='1';
                }            
            }
        }
        /*
        if(mask==8){
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    putchar(s[j][k]);
                }puts("");
            }
        }
        */
        if(mask==8)debug=1;else debug=0;
        if(check1())ans=min(ans,cnt);
        for(int j=0;j<n&&flag;j++){
            for(int k=0;k<n&&flag;k++){
                int tmp=j*n+k;
                if(mask>>tmp&1){
                    s[j][k]='0';
                }            
            }
        }
    }
    printf("%d\n",ans);
}
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int cas=1;
    int _;scanf("%d",&_);
    while(_--){
        printf("Case #%d: ",cas++);
        solve();
    }
}
