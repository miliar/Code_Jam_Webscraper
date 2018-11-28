#include<bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pb push_back
#define mem(a,p) memset(a,p,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define bitcount __builtin_popcount
#define gcd __gcd
#define rep(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
#define sz(a) ((int)(a.size()))
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
#define debug(x,y) cerr<<x<<" "<<y<<" "<<endl;
#define ns ios_base::sync_with_stdio(false);cin.tie(0)
using namespace std;
#define VI vector<int>
#define PII pair<int,int>

double naomi[1200],ken[1200];

int main() {
    int t,n,cs=1;
    freopen("D-large.in","r",stdin);
    freopen("D-output.in","w",stdout);
    scanf("%d",&t);
    while(t--) {
        int cnt=0,cntWar=0,i=0,j=0;
        scanf("%d",&n);
        rep(i,0,n)
        scanf("%lf",&naomi[i]);
        rep(i,0,n)
        scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        //deceitful war;
        while(i<n && j<n) {
            if(naomi[i]<ken[j]) {

            } else {
                ++j;
                ++cnt;
            }
            ++i;
        }
        //second part;only war;
        i=0;
        j=0;
        while(i<n && j<n) {
            if(naomi[i]<ken[j]) {
                i++;
                cntWar++;
            }
            j++;
        }
        printf("Case #%d: %d %d\n",cs++,cnt,n-cntWar);
    }
    return 0;
}

