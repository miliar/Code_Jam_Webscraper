#include<bits/stdc++.h>
using namespace std;
const int N=1111;

double a[N],b[N];
int n;

bool f(int k){
    if(!k) return true;
    int i=n-k;
    for(int j=0;j<k;j++)
        if(a[i+j]<b[j]) return false;
    return true;
}

int deceitful_war(){
    int l=0,r=n;
    while(l+1<r){
        int m=(l+r)/2;
        if(f(m)) l=m;
            else r=m-1;
    }
    while(!f(r)) r--;
    printf("%d",r);

    return 0;
}

int war(){

    set<double> s;
    for(int i=0;i<n;i++) s.insert(b[i]);

    int ans=0;
    for(int i=n-1;i>=0;i--){
        set<double>::iterator j=s.upper_bound(a[i]);
        ans+=j==s.end();
        if(j==s.end()) j=s.begin();
        s.erase(j);
    }

    printf("%d",ans);

    return 0;
}

void solve(){
    scanf("%d",&n);
    for(int i=0;i<n;i++) scanf("%lf",&a[i]);
    for(int i=0;i<n;i++) scanf("%lf",&b[i]);
    sort(a,a+n);
    sort(b,b+n);
    deceitful_war();
    printf(" ");
    war();
}

int main(){
    //freopen("D-large.in","r",stdin);
    //freopen("2.txt","w",stdout);
    //freopen("1.txt","r",stdin);

    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        printf("\n");
    }

    return 0;
}
