#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxs=1020;
char a[maxs];
int T,s;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&T);

    for(int k = 1; k <= T ;k++){
        scanf("%d%s",&s,a);
        //printf("%s\n",a);
        for(int i = 0; a[i]; i++)
            a[i]-='0';
        int cnt = a[0];
        int ans = 0;
        for(int i = 1; i <= s; i++){
            //printf("cnt=%d i=%d\n",cnt,i);
            if(cnt<i){
                ans+=i-cnt;
                cnt+=a[i]+i-cnt;
            }
            else{
                cnt+=a[i];
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
