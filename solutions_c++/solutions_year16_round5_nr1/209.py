#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=100007;
char s[maxn];
int n;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%s",s+1);
        int n=strlen(s+1);
        stack<char> mys;
        int res=0;
        for(int i=1; i<=n; ++i){
            if(sz(mys)==0 || mys.top() != s[i]) mys.push(s[i]);
            else{
                res += 10;
                mys.pop();
            }
        }
        res += (sz(mys)/2)*5;
        printf("Case #%d: %d\n",tt,res);
    }
}

