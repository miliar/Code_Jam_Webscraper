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
typedef pair<int,int> pii;

int a[100],b[100],n;

bool isInc(){
    int i;
    for(i = 1;i<n;i++){
        if(b[a[i-1]] >= b[a[i]]) return false;
    }
    return true;
}
bool isDec(){
    int i;
    for(i = 1;i<n;i++){
        if(b[a[i-1]] <= b[a[i]]) return false;
    }
    return true;
}
bool isZig(){
    int i;
    for(i = 1;i<n;i++){
        if(b[a[i-1]] == b[a[i]]) return false;
        if(b[a[i-1]] > b[a[i]]) break;
    }
    for(;i<n;i++){
        if(b[a[i-1]] == b[a[i]]) return false;
        if(b[a[i-1]] < b[a[i]]) return false;
    }
    return true;
}
int calc(){
    int i,ret = 0,j;
    for(i = 0;i<n;i++){
        for(j = i+1;j<n;j++){
            if(a[i]>a[j]) ret++;
        }
    }
    return ret;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,cs = 1,i,ans;
    cin>>t;
    while(t--){
        cin>>n;
        for(i = 0;i<n;i++){
            cin>>b[i];
            a[i] = i;
        }
        ans = inf;
        do{
            if(isInc() || isDec() || isZig()){
                int r = calc();
                ans = min(r,ans);
            }
        }while(next_permutation(a,a+n));

        printf("Case #%d: %d\n",cs++,ans);
    }
    return 0;
}
