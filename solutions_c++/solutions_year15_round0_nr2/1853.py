#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define UNIQUE(x) (x).resize(distance((x).begin(),unique(all(x))))
int a[10005];
int main() {
    int tc;
    cin>>tc;
    int n;
    for (int kk=0;kk<tc;kk++) {
        cin>>n;
        memset(a,0,sizeof(a));
        int ans=INF,m=0;
        for (int i=0;i<n;i++) {
            cin>>a[i];
            m=max(m,a[i]);
        }
        for (int k=1;k<=m;k++) {
            int r=0;
            for (int i=0;i<n;i++) {
                r+=(a[i]-1)/k;
            }
            ans=min(ans,r+k);
        }
        printf("Case #%d: %d\n", kk+1,ans);
    }
}