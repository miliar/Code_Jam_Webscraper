#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int mx = 105;
char chr[mx];
int Cas;
int main(){
    int n,ans;
    char c1;
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    scanf("%d",&n);
    while(n--){
        scanf("%s",chr);
        c1 = chr[0];
        ans = 0;
        for(int i=1;i<strlen(chr);i++){
            if(c1==chr[i])continue;
            c1 = chr[i];
            ans++;
        }
        if(c1=='-')ans++;
        printf("Case #%d: %d\n",++Cas,ans);
    }
    return 0;
}