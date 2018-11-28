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

double Calculate(double c,double x,double p,double rate) {
    if(x<=c)
        return (double)(x/rate);
    double res=0;
    while(((c/rate)+(x/(rate+p)))<=(x/rate)) {
        res+=c/rate;
        rate+=p;
    }
    return res+x/rate;
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("output_B_large.txt","w",stdout);
    int t,cs=1;
    double c,f,x;
    scanf("%d",&t);
    while(t--) {
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: %.7lf\n",cs++,Calculate(c,x,f,2.0));
    }
    return 0;
}
