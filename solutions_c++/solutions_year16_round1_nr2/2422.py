#include<bits/stdc++.h>
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
using namespace std;
map<int,int> mp;
vector<int> v;
int main() {
    int t,tt,n,i,j;si(t);
    FOR(tt,1,t) {
        mp.clear();
        si(n);
        int N=2*n-1;
        FOR(i,0,N-1) {
            FOR(j,0,n-1) {
                si(a);
                mp[a]++;
            }
        }
        v.clear();
        for(auto it:mp) {
            if(it.second&1) {
                v.push_back(it.first);
            }
        }
        sort(v.begin(), v.end());
        cout<<"Case #"<<tt<<": ";
        for(auto it:v) ps(it);
    }
    return 0;
}
