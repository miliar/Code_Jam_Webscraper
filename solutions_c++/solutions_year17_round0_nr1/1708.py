#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

char rev(char s){
    if(s=='+') return '-';
    return '+';
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; ++tt){
        int k;
        string s;
        cin>>s>>k;
        int res=0;
        for(int i=0; i<sz(s)-k+1; ++i)
            if(s[i]=='-'){
                for(int j=0; j<k; ++j) s[i+j]=rev(s[i+j]);
                ++res;
            }
        for(int i=0; i<sz(s); ++i) if(s[i]=='-'){
            res=-1;
            break;
        }
        printf("Case #%d: ", tt);
        if(res>=0) printf("%d\n",res); else printf("IMPOSSIBLE\n");
    }
}

