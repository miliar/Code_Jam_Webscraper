#include <bits/stdc++.h>
#define ll long long
#define fs first
#define sn second
using namespace std;

FILE * in;
FILE * out;

ll t,n,m,r;
bool u[10];

void res(ll x) {
    while(x) {
        ll digit = x%10;

        if(!u[digit]) {
            r--;
            u[digit]=true;
        }
        x/=10;
    }
}

int main() {
    in = fopen("input.in", "r");
    out = fopen("output.out", "w+");

    fscanf(in,"%lld",&t);

    for(ll k=1;k<=t;k++) {
        r = 10;
        for(ll i=0;i<10;i++)
            u[i]=false;
        fscanf(in,"%lld",&n);
        m = n;
        fprintf(out,"Case #%lld: ",k);

        int c = 0;
        while(r) {
            res(m);
            m+=n;
            c++;
            if(c==1000)
                break;
        }
        if(!r)
            fprintf(out,"%lld",m-n);
        else
            fprintf(out,"INSOMNIA");


        fprintf(out,"\n");
    }

    return 0;
}
