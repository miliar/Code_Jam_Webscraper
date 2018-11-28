#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string.h>
using namespace std;
int key[210];
bool isOpen[30];
int use[30];
vector<int> inside[30];
int ans[30];
int n,k;
int start[30];
bool possible[1<<21];
bool isOkay(){
    int sz=1<<n;
    for(int i=0;i<sz;i++)possible[i]=0;
    int mask=0;
    for(int i=0;i<n;i++)if(isOpen[i]){
        mask|=(1<<i);
    }
    possible[mask]=1;
    for(int i=0;i<sz;i++){
        if(possible[i]){
            int _key[210];
            for(int j=0;j<210;j++)_key[j]=start[j];
            for(int j=0;j<n;j++){
                if(i&(1<<j)){
                    for(int k=0;k<inside[j].size();k++){
                        _key[inside[j][k]]++;
                    }
                    _key[use[j]]--;
                }
            }
            for(int j=0;j<n;j++){
                if(! (i&(1<<j))){
                    if(_key[use[j]]){
                        possible[i|(1<<j)]=1;
                    }
                }
            }
        }
    }
    return possible[sz-1];
}
bool dfs(int now){
    //printf("now==%d\n",now);
    if(now==n){
        for(int i=0;i<n;i++)printf("%d ",ans[i]+1);
        printf("\n");
        return true;
    }
    if(!isOkay()){
        return false;
    }
    for(int i=0;i<n;i++){
        if(!isOpen[i]){
            if(key[use[i]]){
                isOpen[i]=true;
                ans[now]=i;
                key[use[i]]--;
                for(int j=0;j<inside[i].size();j++)
                    key[inside[i][j]]++;
                if(dfs(now+1))return true;
                isOpen[i]=false;
                key[use[i]]++;
                for(int j=0;j<inside[i].size();j++)
                    key[inside[i][j]]--;

            }
        }
    }
    return false;
}
void solve(){
    memset(key,0,sizeof(key));
    memset(isOpen,0,sizeof(isOpen));
    memset(use,0,sizeof(use));
    memset(start,0,sizeof(start));
    for(int i=0;i<=20;i++)inside[i].clear();

    scanf("%d %d",&k,&n);
    for(int i=0;i<k;i++){
        int q;
        scanf("%d",&q);
        key[q]++;
        start[q]++;
    }
    for(int i=0;i<n;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        use[i]=a;
        for(int j=0;j<b;j++){
            int p;
            scanf("%d",&p);
            inside[i].push_back(p);
        }
    }
    if(!dfs(0)){
        printf("IMPOSSIBLE\n");
    }
}
int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
