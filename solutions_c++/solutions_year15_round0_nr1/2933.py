#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
string str;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    int cas = 1;
    while (T--) {
        int x;
        scanf("%d",&x);
        x++;
        cin>>str;
        int ans = 0;
        int tot = 0;
        for (int i = 0; i < x; i++) {
            ans = max(ans,i - tot);
            tot += str[i] - '0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
