#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;
void solve(){
    int n,x;
    scanf("%d %d",&n,&x);
    vector<int> v;
    for(int i = 0 ; i < n ; ++ i ){
        int k;
        scanf("%d",&k);
        v.push_back(k);
    }
    sort(v.rbegin(),v.rend());
    int ans=0;
    for(int i = 0 ; i < n ; ++ i ){
        if(v[i]==-1)continue;
        ans++;
        for(int j = i + 1 ; j < n ; ++ j ){
            if(v[j]!=-1&&v[i]+v[j]<=x){
                v[j]=-1;
                break;
            }
        }
        v[i]=-1;
    }
    printf("%d\n",ans);
}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);

    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ;  ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
