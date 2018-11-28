#include<cstdio>
#include<cstring>

using namespace std;
const int maxn = 1005;

char s[maxn],ans[3*maxn];
int n;

int main(){
    int i,j,cas,l,r;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&cas);
    for(int T=1;T<=cas;T++){
        scanf("%s",s+1);
        n = strlen(s+1);
        l = r = maxn;
        ans[l] = s[1];
        for(i = 2;i <= n;i++){
            if(s[i] >= ans[l]) ans[--l] = s[i];
            else ans[++r] = s[i];
        }
        printf("Case #%d: ",T);
        for(i = l;i <= r;i++) putchar(ans[i]);
        putchar('\n');
    }
    return 0;
}
