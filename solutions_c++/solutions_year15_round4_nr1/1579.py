//Hello. I'm Peter.
//#pragma comment(linker, "/STACK:102400000,102400000")
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<cctype>
#include<ctime>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
using namespace std;
typedef long long ll;
#define peter cout<<"i am peter"<<endl
#define randin srand((unsigned int)time(NULL))
#define INT (0x3f3f3f3f)*2
#define LL (0x3f3f3f3f3f3f3f3f)*2
inline int read(){
	int x=0,f=1;char ch=getchar();
	while(ch>'9'||ch<'0'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
char s[110][110];
int n,m;
bool nosolution(int x,int y){
    for(int i=1;i<=m;i++){
        if(y==i) continue;
        if(s[x][i]!='.') return false;
    }
    for(int i=1;i<=n;i++){
        if(x==i) continue;
        if(s[i][y]!='.') return false;
    }
    return true;
}
int main(){
    //freopen("/Users/peteryuanpan/A/data.txt","r",stdin);
    int T=read();
    for(int kase=1;kase<=T;kase++){
        printf("Case #%d: ",kase);
        n=read(),m=read();
        for(int i=1;i<=n;i++){
            scanf("%s\n",s[i]+1);
        }
        bool ok=true;
        int ans=0;
        for(int i=1;i<=n;i++){
            if(!ok) break;
            for(int j=1;j<=m;j++){
                if(s[i][j]=='.') continue;
                if(nosolution(i,j)){
                    ok=false;
                    break;
                }
                bool find=false;
                if(s[i][j]=='<'){
                    for(int k=1;k<j;k++){
                        if(s[i][k]!='.'){
                            find=true;
                            break;
                        }
                    }
                }
                else if(s[i][j]=='>'){
                    for(int k=j+1;k<=m;k++){
                        if(s[i][k]!='.'){
                            find=true;
                            break;
                        }
                    }
                }
                else if(s[i][j]=='^'){
                    for(int k=1;k<i;k++){
                        if(s[k][j]!='.'){
                            find=true;
                            break;
                        }
                    }
                }
                else if(s[i][j]=='v'){
                    for(int k=i+1;k<=n;k++){
                        if(s[k][j]!='.'){
                            find=true;
                            break;
                        }
                    }
                }
                if(!find) ans+=1;
            }
        }
        if(!ok) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}






