#include <bits/stdc++.h>
using namespace std;
int t;
char s[105];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    for (int i=0;i<t;i++) {
        bool ok=false;
        scanf("%s",s);
        int ans=0;
        int n=strlen(s);
        s[n]='+';
        for (int j=0;j<n;j++) {
            if (s[j]=='+') ok=true;
            if (s[j]=='+'&&s[j+1]=='-') ans++;
            else if (s[j]=='-'&&s[j+1]=='+') ans++;
        }
        if (!ok) printf("Case #%d: 1\n",i+1);
        else printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
