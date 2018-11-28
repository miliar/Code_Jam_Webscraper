#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
char str[1009];

int main(void){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,cou = 1;
    scanf("%d",&t);
    while(t--) {
        scanf("%d%s",&n,str);
        int ans = 0, num = 0;
        for(int i = 0; i <= n; i++) {
            if(num >= i) num += (str[i] - '0');
            else {
                ans += (i - num);
                num = i + (str[i] - '0');
            }
        }
        printf("Case #%d: %d\n", cou++, ans);
    }
    return 0;
}
