#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define inf 0x3f3f3f3f

int x,v[10];
char mp[120];

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0,ans;
    cin>>T;
    while (T--)
    {
        ans=0;
        scanf("%s", mp);
        for (int i=1;i<strlen(mp);i++){
            if (mp[i]!=mp[i-1]) ans++;
        }
        if (mp[strlen(mp)-1] =='-') ans++;
        printf("Case #%d: %d\n", ++cas, ans);
    }
}
