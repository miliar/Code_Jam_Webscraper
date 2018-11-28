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
int t;
int main() {
    cin>>t;
    for (int j=0;j<t;j++) {
        string s;
        int n;
        cin>>n>>s;
        n++;
        int cur=0,ans=0;
        for (int i=0;i<n;i++) {
            int r=s[i]-'0';
            if (cur>=i) {
                cur+=r;
            } else {
                ans+=i-cur;
                cur+=r+i-cur;
            }
        }
        printf("Case #%d: %d\n",j+1,ans);
    }
}