#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char s[105];
void solve(){
    scanf("%s",s);
    int len = strlen(s);
    int res = 1;
    for(int i = 1 ; i < len ; i ++){
        if(s[i] != s[i - 1]) res ++;
    }
    if(s[len - 1] == '+') res --;
    printf("%d\n",res);
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _,txt = 1;
    scanf("%d",&_);
    while(_--){
        printf("Case #%d: ",txt ++);
        solve();
    }
    return 0;
}
