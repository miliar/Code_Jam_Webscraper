#include <bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
const int MX=1233;
string str;
int n;
int solve(){
    int iter=0 , ans=0 , cur=2;
    if(str[1] == '-') ans++;
    while(1){
        if(cur > n) break;
        if(str[cur] == '-' && str[cur-1]=='+')
            ans++;
        cur++;
    }
    ans*=2;
    if(str[1]=='-') ans--;
    return ans;
}
int main(){
    /*#ifdef ONLINE_JUDGE
    freopen("high.in","r",stdin);
    freopen("high.out","w",stdout);
    #endif // ONLINE_JUDGE*/
    //#ifndef ONLINE_JUDGE
    //freopen("in.in","r",stdin);
    //freopen("out.out","w",stdout);
    //#endif // ONLINE_JUDGE*/
    int T , Tn=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++Tn);
        cin>>str;
        n = str.size();
        str="#"+str;
        cout<<solve()<<endl;
    }

}

