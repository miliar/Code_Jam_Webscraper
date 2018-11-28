#include<bits/stdc++.h>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int a[10004];
bool used[10004];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cs=1,i,j,k,ii,x,n,ans ;
    cin>>t;
    while(t--){
        cin>>n>>x;
        for(i = 0;i<n;i++)
            cin>>a[i], used[i] = 0;
        sort(a,a+n,greater<int>());
        ans = 0;
        for(i = 0;i<n;i++){
            if(used[i]) continue;
            k = x - a[i];
            int mx = 0;
            for(j = i+1;j<n;j++){
                if(used[j] || a[j]>k) continue;
                if(a[j]>mx){
                    mx = a[j];
                    ii = j;
                }
            }
            if(mx ){
                used[ii] = 1;
                used[i] = 1;
                ans++;
            }
            else {
                used[i] = 1;
                ans++;
            }
        }

        printf("Case #%d: %d\n",cs++,ans);
    }
	return 0;
}
