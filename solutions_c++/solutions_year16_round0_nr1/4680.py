#include <cstdio>
#include <cstring>
using namespace std;
bool flag[10];
bool check() {
    for(int i=0; i<10; ++i)
        if(!flag[i])
            return false;
    return true;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%d",&n);
        printf("Case #%d: ",cas);
        if(n==0) {
            puts("INSOMNIA");
            continue;
        }
        memset(flag,false,sizeof(flag));
        int ans=0;
        do {
            ans+=n;
            for(int num=ans; num; num/=10)
                flag[num%10]=true;
        } while(!check());
        printf("%d\n",ans);
    }
    return 0;
}
