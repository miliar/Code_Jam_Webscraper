#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
typedef long long LL;
const int N=100+10;
const int Maxn=10000000;
vector<LL> q;
bool check(LL x){
    int s[32],sz=0;
    while (x){
        s[sz++]=x%10;
        x/=10;
    }
    for (int i=0;i<sz/2;i++){
        if (s[i]!=s[sz-i-1]) return 0;
    }
    return 1;
}
void init(){
    q.clear();
    for (int i=1;i<=Maxn;i++){
        if (check((LL)i) && check((LL)i*i)){
            q.push_back((LL)i*i);
        }
    }
   /* for (int i=0;i<q.size();i++){
        cout<<q[i]<<" ";
    }cout<<endl;
*/
}
LL A,B;
int main(){
    init();
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;cin>>T;
    int sz=q.size();
    while (T--){
        cin>>A>>B;

        int ret=0;
        for (int i=0;i<sz;i++){
            if (A<=q[i] && q[i]<=B) ret++;
        }
        printf("Case #%d: %d\n",++cas,ret);
       // cout<<A<<" "<<B<<endl;
    }
    return 0;
}
