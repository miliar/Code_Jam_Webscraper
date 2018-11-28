#include<bits/stdc++.h>
using namespace std;;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t; scanf("%d",&t);
    int j=1;
    while(t--){
        string s; cin >> s;
        int i,n = s.length();
        i = n-1; int ans=0;
        while(s[i]=='+' && i>=0)
            i--;
        while(i>=0){
            while(s[i]=='-' && i>=0)
                i--;
            ans++;
            if(i==-1)
                break;
            while(s[i]=='+' && i>=0)
                i--;
            ans++;
            if(i==-1)
                break;
        }
        printf("Case #%d: %d\n",j,ans);
        j++;
    }
    return 0;
}
