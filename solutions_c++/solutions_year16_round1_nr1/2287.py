#include<cstdio>
#include<queue>
#include<climits>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<ctype.h>
#include<set>
#include<vector>
#include<map>
#include<time.h>
#include<list>
#include<iostream>
#include<stack>
using namespace std;
#define mod 1000000007
#define mem(x) memset(x,0,sizeof(x))
#define pri printf
#define sca scanf

typedef long long LL;
const double PI=acos(-1.0);
const double  eps=1e-9;
//freopen("D.out","w",stdout);
string s,ss,ans;
int main(){
    int n,i,j,m;
    int T;
    freopen("A-large.in","r",stdin);
    freopen("D.out","w",stdout);
    sca("%d",&T);
    for (int cas=1;cas<=T;cas++){
        cin>>s;
        n=s.size();
        ans=s[0];
        for (i=1;i<n;i++)
        {
            ss=s[i];
            if (ans[0]<=s[i]) {
                ans=ss+ans;
            }
            else
            {
                ans=ans+ss;
            }
        }
        pri("Case #%d: ",cas);
        cout<<ans<<endl;

    }
    return 0;
}





















