#include <bits/stdc++.h>
using namespace std;

char s[110];

bool ok(){
    for(int i=0;s[i];i++){
        if(s[i]=='-') return false;
    }
    return true;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%s",s);
        printf("Case #%d: ",ca);
        int ans=0;
        while(1){
            if(ok()) break;
            int l=0;
            while(s[l]=='+') l++;
            int r=strlen(s)-1;
            while(s[r]=='+') r--;
            if(l){
                for(int j=0;j<l;j++) s[j]='-';
                ans++;
            }
            if(r) reverse(s,s+r+1);
            for(int j=0;j<=r;j++){
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
