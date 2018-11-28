#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)

char rev(char a){
    return (a=='-')?'+':'-';
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    string s;
    int n,k;
    forn(i,t){
        cin>>s>>k;
        n = s.length();
        int ans = 0;
        for(int i=0;i<=n-k;++i){
            if(s[i]=='-'){
                ++ans;
                for(int j=0;j<k;++j)
                    s[i+j] = rev(s[i+j]);

              //  cout<<s<<'\n';
            }
        }
        bool g = 1;
        for(int i=n-k;i<n;++i)
            if(s[i]=='-')
                g = 0;

        if(g)
            printf("Case #%d: %d\n",i+1,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",i+1);
    }
}
