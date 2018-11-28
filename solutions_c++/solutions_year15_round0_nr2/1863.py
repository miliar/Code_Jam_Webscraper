#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <stack>
#include <string>
#include <map>

using namespace std;
int n,P[110000];
int solve(){
    cin>>n;
    int ans=1e9;
    for(int i=0;i<n;i++){
        cin>>P[i];
    }
    for(int t=1;t<=ans;t++){
        int cur=0;
        for(int j=0;j<n;j++){
            if(P[j]>t)cur+=(P[j]-1)/t;
        }
        ans=min(ans,cur+t);
    }
    return ans;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}
