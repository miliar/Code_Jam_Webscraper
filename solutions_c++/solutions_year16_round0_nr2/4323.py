#include<bits/stdc++.h>
using namespace std;

typedef __int64 ll;

int n;
char s[111];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("text.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++) {
        scanf("%s",s);
        n=strlen(s);
        int num=0;
        for(int i=1;i<n;i++) if(s[i]!=s[i-1]) num++;
        if(s[n-1]=='-') num++;
        printf("Case #%d: %d\n",ca,num);
    }
    return 0;
}
