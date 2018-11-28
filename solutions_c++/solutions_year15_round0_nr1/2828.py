#include <iostream>
#include <cstdio>
typedef long long Lint;
using namespace std;

char s[1111];
Lint n,T,cur,ans,cas=0;

int main(){
    freopen("data.in","rb",stdin);
    freopen("data.out","wb",stdout);
    cin>>T;
    while (T--){
        cin>>n>>s;
        cur=ans=0;
        for (Lint i=0; s[i]; i++){
            if (cur<i){
                ans+=i-cur;
                cur=i;
            }
            cur+=s[i]-'0';
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
        //printf("Case #%d: %d\n",++cas,ans);
    }
}
