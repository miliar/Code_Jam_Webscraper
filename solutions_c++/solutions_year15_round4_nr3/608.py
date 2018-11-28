#include<bits/stdc++.h>
using namespace std;
map<string,int> ma;
vector<int> arr[20];
char c[20005],in[20005];
int ans,a[20005],b[20005],n,top;
void dfs(int u){
    int i;
    if(u==n){
        int tmp=0;
        for(i=1;i<=top;i++){
            if(a[i]&& b[i]) tmp++;
        }
        if(ans==-1 || tmp<ans) ans=tmp;
        return;
    }
    if(u!=1){
        int pre[15];
        for(i=0;i<arr[u].size();i++){
            int v=arr[u][i];
            pre[i]=a[v],a[v]=1;
        }
        dfs(u+1);
        for(i=0;i<arr[u].size();i++){
            int v=arr[u][i];
            a[v]=pre[i];
        }
    }
    if(u!=0){
        int pre[15];
        for(i=0;i<arr[u].size();i++){
            int v=arr[u][i];
            pre[i]=b[v],b[v]=1;
        }
        dfs(u+1);
        for(i=0;i<arr[u].size();i++){
            int v=arr[u][i];
            b[v]=pre[i];
        }
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int t,C=0,m,i,j;
    double a1,b1,c1,a2,b2,c2,V,X,q,w;
    scanf("%d",&t);
    while(t--){
        scanf("%d\n",&n);
        ans=-1;
        ma.clear();
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for(i=0;i<20;i++) arr[i].clear();
        for(j=0;j<n;j++){
            gets(in);
            for(i=0;in[i];i++){
                if(i==0 || in[i-1]==' '){
                    sscanf(&in[i],"%s",c);
                    if(ma[string(c)]==0) ma[string(c)]=ma.size();
                    arr[j].push_back(ma[string(c)]);
                    //printf("%d..",ma[string(c)]);
                }
            }//puts("");
        }
        top=ma.size();
        dfs(0);
        printf("Case #%d: %d\n",++C,top);
    }
}


