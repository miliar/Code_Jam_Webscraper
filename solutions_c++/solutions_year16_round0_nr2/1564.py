#include<cstdio>
#include<cstring>
using namespace std;
int T,t,n,m,ans;
char s[110];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        ans=0;
        scanf("%s",s+1);
        n=strlen(s+1);
        char c='+';
        for(i=n;i>=1;i--){
            if(c==s[i])
                continue;
            else{
                ans++;
                if(c=='+')
                    c='-';
                else
                    c='+';
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
