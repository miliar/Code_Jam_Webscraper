#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

vector<double> P;

void solve(int por) {
    int n,k;
    scanf("%d %d",&n,&k);
    P.clear(); P.resize(n);
    For(i,n) scanf(" %lf",&P[i]);
    vector<double> A;
    double res=0;
    For(i,1<<n) {
        int p=0;
        For(j,n) if(i&(1<<j)) p++;
        if(p!=k) continue;
        A.clear();
        For(j,n) if(i&(1<<j)) A.push_back(P[j]);
        double vys=0.0;
        For(j,1<<k) {
            double v=1.0;
            int pp=0;
            For(p1,k) if(j&(1<<p1)) pp++;
            if(pp!=k/2) continue;
            For(p1,k)
                if(j&(1<<p1)) v*=A[p1];
                else v*=(1-A[p1]);
            vys+=v;
        }
        res=max(res,vys);
    }
    printf("Case #%d: %0.9lf\n",por,res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
