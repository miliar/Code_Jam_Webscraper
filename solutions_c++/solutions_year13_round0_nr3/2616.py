#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T,A,B;
bool judge(int k) {
     char ch[30];
     int l;
     sprintf(ch,"%d",k);
     l = strlen(ch);
     bool flag = true;
     for (int i = 0;i < l; i++)
         if (ch[i] != ch[l-i-1]) {flag = false; break;}
     return flag;
}
bool f[1100];
int ans[1100];
int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    memset(f,0,sizeof(f));
    for (int i = 1;i <= 1000; i++) {
        if (judge(i) && i*i <= 1000 && judge(i*i) )  f[i*i] = true;
    }
    ans[0] = 0;
    for (int i = 1;i <= 1000; i++){ ans[i] = ans[i-1]; if (f[i]) ans[i]++;} 
    cin>>T;
    for (int kase = 1;kase <= T; kase++) {
        cin>>A>>B;
        printf("Case #%d: %d\n",kase,ans[B]-ans[A-1]);
    }
    return 0;
}
