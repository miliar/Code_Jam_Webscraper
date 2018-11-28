#include<bits/stdc++.h>
using namespace std;
char s[105][105];
int l[105],r[105],u[105],d[105];
int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out","w",stdout);
    int t,C=0,n,m,i,j,x,y;
    scanf("%d",&t);
    while(t--){
        int ans=0;
        memset(l,-1,sizeof(l));
        memset(r,-1,sizeof(r));
        memset(u,-1,sizeof(u));
        memset(d,-1,sizeof(d));
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++){
            scanf("%s",s[i]);
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++) if(l[i]==-1 && s[i][j]!='.') l[i]=j;
            for(j=m-1;j>=0;j--) if(r[i]==-1 && s[i][j]!='.') r[i]=j;
        }
        for(j=0;j<m;j++){
            for(i=0;i<n;i++) if(u[j]==-1 && s[i][j]!='.') u[j]=i;
            for(i=n-1;i>=0;i--) if(d[j]==-1 && s[i][j]!='.') d[j]=i;
        }
        int flag=1;
        for(i=0;i<n;i++){
            if(l[i]==r[i] && l[i]!=-1 && (s[i][l[i]]=='<' || s[i][l[i]]=='>')) flag=0;
            else{
                if(s[i][l[i]]=='<') ans++;
                if(s[i][r[i]]=='>') ans++;
            }
        }
        for(i=0;i<m;i++){
            if(u[i]==d[i] && u[i]!=-1 && (s[u[i]][i]=='^' || s[u[i]][i]=='v')) flag=0;
            else{
                if(s[u[i]][i]=='^') ans++;
                if(s[d[i]][i]=='v') ans++;
            }
        }
        printf("Case #%d: ",++C);
        if(flag) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
}
