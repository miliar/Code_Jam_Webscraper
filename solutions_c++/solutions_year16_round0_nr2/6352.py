#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
char ch[110];
void rev(int r){
    for(int i=0;i<r/2;i++) {
        swap(ch[i], ch[r - 1 - i]);
    }
}
void ops(int r){
    for(int i=0;i<r;i++) {
        ch[i] = '-' + '+' - ch[i];
    }
}
int main() {
    freopen("Blarge.in","r",stdin);
    freopen("BLout.out","w",stdout);
    int T;scanf("%d",&T);
    for(int tt = 1;tt <= T;tt++) {
        scanf("%s",ch);
        int r = strlen(ch);
        while(r > 0 && ch[r - 1] == '+') r--;
        int ans = 0;
        while(r > 0) {
            if(ch[0] == '+') {
                int l = 0;
                while(ch[l] == '+') l++;
                rev(l);ops(l);ans++;
            }
            rev(r);ops(r);ans++;
            while(r > 0 && ch[r - 1] == '+') r--;
            //printf("%s\n",ch);
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
