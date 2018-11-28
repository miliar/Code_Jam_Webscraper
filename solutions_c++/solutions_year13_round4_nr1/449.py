#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

#define NN 2100
int cap[NN][NN];
int flow[NN][NN];

long long cost_of(long long n, long long u, long long v) {
    long long d = v - u + 1;
    return (n-d+1+n)*d/2;
}

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){

        long long n;
        int m;
        scanf("%lld%d", &n, &m);

        long long Path[m][3];
        vector<long long> A;
        long long old_cost = 0;
        for (int i=0;i<m;i++) {
            long long u,v,x;
            scanf("%lld%lld%lld", &u, &v, &x);
            Path[i][0] = u;
            Path[i][1] = v;
            Path[i][2] = x;
            A.push_back(u);
            A.push_back(v);

            old_cost += cost_of(n, u, v) * x;
        }
        sort(A.begin(), A.end());
        A.erase(unique(A.begin(), A.end()), A.end());
        
        int N = A.size();
        long long in[N], out[N];
        memset(in, 0, sizeof(in));
        memset(out, 0, sizeof(out));
        for (int i=0;i<m;i++) {
            int u = lower_bound(A.begin(), A.end(), Path[i][0]) - A.begin();
            int v = lower_bound(A.begin(), A.end(), Path[i][1]) - A.begin();
            in[u] += Path[i][2];
            out[v] += Path[i][2];
        }

        /*
        for (int i=0;i<N;i++) {
            printf("%lld %lld\n", in[i], out[i]);
        }
        */

        long long new_cost = 0;

        for (int i=N-1;i>=0;i--) {
            while (in[i] > 0) {
                for (int j=i;j<N;j++) {
                    if (out[j] > 0) {
                        //printf("%d %d: %lld %lld\n", j, i, out[j], in[i]);
                        long long diff = min(out[j], in[i]);
                        out[j] -= diff;
                        in[i] -= diff;
                        new_cost += diff * cost_of(n, A[i], A[j]);
                    }
                }
            }
        }

        long long ans = old_cost - new_cost;

        printf("Case #%d: %lld\n",ti,ans);
    }
    return 0;
}
