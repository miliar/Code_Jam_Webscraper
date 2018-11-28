#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <algorithm>

using namespace std;

#define MP make_pair
typedef long long LL;
int a[101];
int A,n;
const int inf = 1000000;

LL hash(int pre,int u){
    return (long long)pre*1000+u;
}

int dfs(int pre,int u,map<LL,int> mp){
    if(u==n) return 0;
    if(mp.find(hash(pre,u))!=mp.end()) return mp[hash(pre,u)];
    int ans = inf;
    if(pre>a[u]){
        ans = dfs(pre+a[u],u+1,mp);
    }else{
        ans = min(dfs(pre,u+1,mp)+1,ans);
        if(pre!=1){
            int tmp = pre;
            int cnt = 0;
            while(tmp<=a[u]){
                tmp+=tmp-1;
                cnt++;
            }
            ans = min(dfs(tmp+a[u],u+1,mp)+cnt,ans);
        }
    }
    mp.insert(MP(hash(pre,u),ans));
    return ans;
}

int main(void){
    freopen("D:\\acm.txt","r",stdin);
    freopen("D:\\acm2.txt","w",stdout);
    int t,tt = 1;
    cin>>t;
    while(t--){
        cin>>A>>n;
        map<long long,int> mp;
        for(int i = 0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);
        cout<<"Case #"<<tt++<<": "<<dfs(A,0,mp)<<endl;
    }

}
