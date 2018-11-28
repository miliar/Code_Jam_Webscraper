#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("3.out", "w", stdout);
    int t,cas=1,l,i,ans;
    char s[105];
    scanf("%d", &t);
    while(t--){
        scanf("%s", s);
        l=strlen(s);
        ans=0;
        for(i=l-1;i>=0;i--){
            if(ans%2==1 && s[i]=='+') ans++;
            else if(ans%2==0 && s[i]=='-') ans++;
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
