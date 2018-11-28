#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
    int cs;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        int n,a[1005],ans=1005,top=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            top=max(top,a[i]);
        }
        for(int c=1;c<=top;c++){
            int use=c;
            for(int i=0;i<n;i++) use+=(a[i]-1)/c;
            ans=min(ans,use);
        }
        printf("Case #%d: %d\n",no,ans);
    }
}