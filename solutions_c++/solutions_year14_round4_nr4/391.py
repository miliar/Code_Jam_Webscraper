#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

const int maxn=1e3+5;

int n,m;
char s[10][100];
int ch[200][26],f[10];
int sz,ans,sum;
string str[10];

void ini(){
    sz=1;
    memset(ch[0],-1,sizeof(ch[0]));
}

void add(char s[]){
    int now=0;
    for(int i=0;s[i];i++){
        if(ch[now][s[i]-'A']==-1)
        {
            memset(ch[sz],-1,sizeof(ch[sz]));
            ch[now][s[i]-'A']=sz++;
        }
        now=ch[now][s[i]-'A'];
    }
}

void dfs(int x){
    if(x==n){
        int ss=0;
        for(int i=0;i<m;i++){
            ini();
            for(int j=0;j<n;j++)
                if(f[j]==i){
                    add(s[j]);
                }
            if(sz==1)return;
            ss+=sz;
        }
        if(ss>ans)ans=ss,sum=1;
        else if(ss==ans)sum++;
        return;
    }
    for(int i=0;i<m;i++)
    {
        f[x]=i;
        dfs(x+1);
    }
}

int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%s",s[i]);
        ans=sum=0;
        dfs(0);
        printf("Case #%d: %d %d\n",cas,ans,sum);
    }
    return 0;
}
