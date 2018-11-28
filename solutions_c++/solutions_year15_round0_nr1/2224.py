//#define LOCAL
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int Cas;
char chr[1005];
int main(){
    #ifdef LOCAL
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    #endif
    int T,ans,s,cnt;
    scanf("%d",&T);
    while(T--){
        ans = 0;
        cnt =0;
        scanf("%d%s",&s,chr);
        for(int i=0;i<strlen(chr);i++){
            if(chr[i]== '0' && cnt == 0)ans++;
            else cnt += chr[i]-'1';
        }
        printf("Case #%d: ",++Cas);
        printf("%d\n",ans);
    }
    return 0;
}
