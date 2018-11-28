#include <cstdlib>
#include <iostream>
const int maxn = 1111;
char s[maxn];

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,cas=1;
    scanf("%d",&T);
    while(T--) {
        scanf("%d %s",&n,s);
        int sum = 0;
        int ans = 0;
        for(int i=0;i<=n;i++){
            if(sum>=i){
                sum+=s[i]-'0';
            }else{
                ans+=i-sum;
                sum+=i-sum+s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",cas++,ans);;
    }
    
    return 0;
}
