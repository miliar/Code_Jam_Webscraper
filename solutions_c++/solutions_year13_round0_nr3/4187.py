#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

static long long fs[100], idx=0;

long bsearch(long long val){
    long long s=0, e=idx, mid;
    while(e-s>1){
        mid=(s+e)/2;
        if (val>=fs[mid]) s=mid;
        else if (val<fs[mid]) e=mid;
    }
    if (val<fs[s]) return s;
    else if (val<fs[e]) return e;
    else return e+1;
}

int chkpl(long long n){
    long long m=n, temp=0, q;
    while(m>0){
        q=m%10;
        temp=temp*10+q;
        m/=10;
    }
    return (temp==n)? 1:0;
}

void precompute(){
    for (long long i=1; i<=10000000; ++i){
        if (chkpl(i) && chkpl(i*i)) fs[++idx]=i*i;
    }
}

int main()
{
    freopen("in1.in", "r", stdin);
    freopen("out1.out", "w", stdout);
    precompute(); fs[++idx]=1000000000000000;
    long long s, e;

    int T; cin >> T;
    for(int t=1; t<=T; ++t){
        cin >> s >> e;
        cout << "Case #" << t << ": " << bsearch(e)-bsearch(s-1) << '\n';
    }
    return 0;
}
