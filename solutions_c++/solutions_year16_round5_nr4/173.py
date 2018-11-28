#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
//    freopen("input.txt","r",stdin);
    int T,n,l;
    cin>>T;
    for(int tt=1; tt<=T; ++tt){
        printf("Case #%d: ",tt);
        string s;
        cin>>n>>l;
        bool found=0;
        for(int i=1; i<=n; ++i){
            cin>>s;
            bool t=1;
            for(int j=0; j<sz(s); ++j) if(s[j]!='1') t=0;
            if(t) found=1;
        }
        cin>>s;
        if(found) puts("IMPOSSIBLE");
        else{
            if(l==1){
                puts("? 0");
            }else{
                for(int i=1; i<l; ++i) printf("?");
                printf(" ");
                printf("10?1");
                for(int i=1; i<(l+1)/2; ++i) printf("01");
                puts("");
            }
        }

    }
}
