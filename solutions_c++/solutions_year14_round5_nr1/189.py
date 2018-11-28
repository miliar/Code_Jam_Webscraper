//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n;
ll p,q,r,s;
ll A[1000047];

inline int num(int i){
    return (i*p+q)%r + s;
}

bool check(ll m){
    ll sum, pos = 0;
    For(i, 3){
        sum = 0;
        while(pos<n && sum+A[pos]<=m) {
            sum+=A[pos];
            pos++;
        }
    }
    return (pos == n);
}

int extra(){
    scanf("%d%lld%lld%lld%lld",&n,&p,&q,&r,&s);
    ll sum = 0;
    For(i, n) sum += (A[i] = num(i));
    //if (n<21){
    //    For(i, n) printf("%d, ", A[i]);
    //    printf("\n");
    //}
    ll b = 0, e = sum, m;
    while(e-b>1){
        m = (b+e)/2;
        if (check(m)) e = m;
        else b = m;
    }
    //printf("%lld\n", e);
    printf("%.12lf\n",1.-double(e)/double(sum));
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
