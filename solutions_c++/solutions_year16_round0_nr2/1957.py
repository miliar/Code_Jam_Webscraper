#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int solve(string s){
    while(sz(s)>0 && s[sz(s)-1]=='+') s.erase(sz(s)-1,1);
    if(s.empty()) return 0;
    int res=1;
    for(int i=1; i<sz(s); ++i) if(s[i-1]!=s[i]) ++res;
    return res;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        string s;
        cin>>s;
        printf("Case #%d: %d\n",tt,solve(s));
    }
}

