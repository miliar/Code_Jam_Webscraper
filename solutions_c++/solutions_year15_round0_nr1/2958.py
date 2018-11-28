#include <cstdio>
using namespace std;

int main(){
    int cs;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        int n,x,cnt=0,use=0;
        scanf("%d",&n);
        for(int i=0;i<=n;i++){
            scanf("%1d",&x);
            if(cnt<i){
                int w=i-cnt;
                use+=w;
                cnt+=w;
            }
            cnt+=x;
        }
        printf("Case #%d: %d\n",no,use);
    }
}