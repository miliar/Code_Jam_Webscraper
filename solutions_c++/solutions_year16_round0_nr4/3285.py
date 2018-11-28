#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int inf=1e6+10;
typedef __int64 LL;
int k,c,s;
LL fun(int a,int b){
    LL ans=1;
    for(int i=a;i<=b;i++){
        ans=(ans-1)*k+i;
    }
    return ans;
}
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T;scanf("%d",&T);int cas=1;
    while(T--){
        printf("Case #%d:",cas++);
        scanf("%d%d%d",&k,&c,&s);
        if((k+c-1)/c>s)printf("IMPOSSILBE\n");
        else {
            for(int i=1;i<=s;i++){
                if(i*c<k){
                    printf(" %I64d",fun((i-1)*c+1,i*c));
                }
                else {
                    printf(" %I64d",fun((i-1)*c+1,k));
                    printf("\n");
                    break;
                }
            }
        }
    }
    return 0;
}
