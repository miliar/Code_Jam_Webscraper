#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int o[1005];
string a[1005];

class TrieGraph {
public:
    static const int SIZE = 105;
    static const int LEAF = 26;
    int next[SIZE],e[SIZE][LEAF],n;
    int data[SIZE];
    TrieGraph(){n=SIZE;}
    void init(){
        fill_n(next,n,0);
        fill_n(data,n,0);
        memset(e,-1,n*sizeof(e[0]));
        n=1;
    }
    void insert(const char* s, int idx = 0){
        int x=0;
        for(int i=0;s[i];i++){
            int c=s[i]-'A';
            x=~e[x][c]?e[x][c]:e[x][c]=n++;
        }
        data[x]|=1<<idx;
    }
    void make(){
        static int q[SIZE],m;
        next[0]=m=0;
        for(int c=0;c<LEAF;c++)
            if(~e[0][c]) next[q[m++]=e[0][c]]=0; else e[0][c]=0;
        for(int i=0;i<m;i++){
            int x=q[i];
            data[x]|=data[next[x]];
            for(int c=0;c<LEAF;c++){
                int t=e[next[x]][c];
                if(~e[x][c]) next[q[m++]=e[x][c]]=t; else e[x][c]=t;
            }
        }
    }
};

int ans,way;

void dfs(int x, int n, int m){
    if(x==m){
        int cnt=0;
        TrieGraph g[10];
        for(int i=0;i<n;i++) g[i].init();
        for(int i=0;i<m;i++) g[o[i]].insert(a[i].c_str());
        for(int i=0;i<n;i++) cnt+=g[i].n;
        for(int i=0;i<n;i++) if(g[i].n==1) return;
        if(cnt==ans) way++;
        if(cnt> ans){
            ans=cnt;
            way=1;
        }
        return;
    }
    for(o[x]=0;o[x]<n;o[x]++) dfs(x+1,n,m);
}

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int m,n;
        scanf("%d%d",&m,&n);
        for(int i=0;i<m;i++){
            char str[105];
            scanf("%s",str);
            a[i]=str;
        }
        ans=way=0;
        dfs(0,n,m);
        printf("Case #%d: %d %d\n",++no,ans,way);
    }
}
