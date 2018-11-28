#include <bits/stdc++.h>
using namespace std;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};
char s[200][200];
int n,m;
map<char,int> mm;


bool hefa(int x, int y) {
    if(x>=1&&x<=n&&y>=1&&y<=m)
        return true;
    return false;
}

int work() {
    int ans=0;
    int i,j;
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++){
            if(s[i][j]=='.')
                continue;
            int w=mm[s[i][j]];
            ///cout<<w<<endl;
            int x=i,y=j;
            int flag=1;
            while(true){
                x+=dx[w];
                y+=dy[w];
                if(!hefa(x,y)) {
                    flag=0;
                    break;
                }
                if(s[x][y]!='.')
                    break;
            }
            if(flag)
                continue;
            flag=0;
            ans++;
            for(int ii=0;ii<4;ii++) {
                if(ii==w)
                    continue;
                x=i;
                y=j;
                bool ok=true;
                while(true){
                    x+=dx[ii];
                    y+=dy[ii];
                    if(!hefa(x, y)) {
                        ok=false;
                        break;
                    }
                    if(s[x][y]!='.')
                        break;
                }
                if(ok){
                    flag=1;
                    break;
                }
            }
            if(!flag)
                return -1;
        }
    return ans;
}

int main() {
    int t;
    int cas=0;
    scanf("%d",&t);
    mm['>']=0;
    mm['v']=1;
    mm['<']=2;
    mm['^']=3;
    mm['.']=-1;
    while(t--) {
        scanf("%d%d", &n,&m);
        int i;
        for(i=1;i<=n;i++)
            scanf("%s",s[i]+1);
        printf("Case #%d: ", ++cas);
        int ans=work();
        if(ans==-1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}