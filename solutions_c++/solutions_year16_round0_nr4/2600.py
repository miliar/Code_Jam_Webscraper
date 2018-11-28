#include <bits/stdc++.h>
#define ll long long
#define fs first
#define sn second
using namespace std;

FILE * in;
FILE * out;

ll t,k,c,s;
ll res[105];

int main() {
    in = fopen("input.in", "r");
    out = fopen("output.out", "w+");

    fscanf(in,"%lld",&t);

    for(ll K=1;K<=t;K++) {
        fscanf(in,"%lld %lld %lld",&k,&c,&s);
        fprintf(out,"Case #%lld:",K);

        for(int i=1;i<=k;i++)
            res[i] = i;

        for(int i=2;i<=k;i++)
            for(int j=0;j<c-1;j++)
                res[i] = k * res[i] - (k - i);

        for(int i=1;i<=k;i++)
            fprintf(out," %lld",res[i]);

        fprintf(out,"\n");
    }

    return 0;
}
