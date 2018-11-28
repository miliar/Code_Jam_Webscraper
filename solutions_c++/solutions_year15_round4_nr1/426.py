#include<bits/stdc++.h>
using namespace std;
char s[105][105];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T; cin>>T;
    for(int cs=1; cs<=T; cs++){
        int n, m; cin>>n>>m;
        int ans=0;
        for(int i=0; i<n; i++){
            scanf("%s",s[i]);
        }
        printf("Case #%d: ",cs);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(s[i][j]=='.') continue;
                if(s[i][j]=='^'){
                    int k=i-1;
                    while(k>=0&&s[k][j]=='.'){
                        k--;
                    }
                    if(k<0) ans++;
                }
                if(s[i][j]=='v'){
                    int k=i+1;
                    while(k<n&&s[k][j]=='.'){
                        k++;
                    }
                    if(k>=n) ans++;
                }
                if(s[i][j]=='<'){
                    int k=j-1;
                    while(k>=0&&s[i][k]=='.'){
                        k--;
                    }
                    if(k<0) ans++;
                }
                if(s[i][j]=='>'){
                    int k=j+1;
                    while(k<m&&s[i][k]=='.'){
                        k++;
                    }
                    if(k>=m) ans++;
                }
                int cnt=0;
                int k=i-1;
                while(k>=0&&s[k][j]=='.'){
                    k--;
                }
                if(k<0) cnt++;
                k=i+1;
                while(k<n&&s[k][j]=='.'){
                    k++;
                }
                if(k>=n) cnt++;
                k=j-1;
                while(k>=0&&s[i][k]=='.'){
                    k--;
                }
                if(k<0) cnt++;
                k=j+1;
                while(k<m&&s[i][k]=='.'){
                    k++;
                }
                if(k>=m) cnt++;
                if(cnt==4){
                    goto failed;
                }
            }
        }
        printf("%d\n",ans);
        continue;
        failed:;
        puts("IMPOSSIBLE");
    }
    return 0;
}
