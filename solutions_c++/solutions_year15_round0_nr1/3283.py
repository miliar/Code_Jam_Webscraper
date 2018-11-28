#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
const int M = 1100;
char s[M];

int main()
{
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int T,maxn,pre,num,cnt = 0;
    cin>>T;
    while(T--) {
        scanf("%d %s",&maxn,s);
        pre = s[0] - '0';
        num = 0;
        for(int i = 1; i <= maxn; i++) {
            if(s[i] == '0') continue;
            if(pre >= i) pre += s[i] - '0';
            else {
                num += i - pre;
                pre += i - pre + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n",++cnt,num);
    }
    return 0;
}
//
