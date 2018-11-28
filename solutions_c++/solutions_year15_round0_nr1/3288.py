#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

char s[10000];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,cas=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        scanf("%s",s);
        int tmp = 0;
        int ans = 0;
        for(int i=0;s[i];i++){
            int now= s[i]-'0';
            if(tmp >= i){
                tmp += now;
            }else if(tmp<i && now>0){
                ans += i-tmp;
                tmp = i + now;
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
