#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;
int main(){
freopen("1b.txt","r",stdin);
freopen("1bans.txt","w",stdout);
int t,a,b,k;
scanf("%d",&t);
for(int v=1;v<=t;v++)
{
    int cnt=0;
    scanf("%d%d%d",&a,&b,&k);
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            if((i&j)<k)
                cnt++;
        }
    }
    printf("Case #%d: %d\n",v,cnt);
}
return 0;
}
