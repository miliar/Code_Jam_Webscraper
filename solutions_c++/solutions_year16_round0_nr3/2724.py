#include <bits/stdc++.h>
#define ll unsigned long long
#define fs first
#define sn second
#define lim 100000000
using namespace std;

FILE * in;
FILE * out;

ll t, n = 32769, j = 50;
ll np, primes[10000001];
ll criba[100000001];

ll p(ll a, ll b) {
    if(!b) return 1;
    ll sqr = p(a,b/2);
    if(b%2 == 0) return sqr * sqr;
    return sqr * sqr * a;
}

ll toBin(ll x) {
    ll r=0;

    for(ll i=0;x;i++) {
        r += (x%2) * p(10,i);
        x /= 2;
    }

    return r;
}

ll toBase(ll x, ll b) {
    ll num = 0;

    for(ll i=0;x;i++) {
        num += (x%10) * p(b,i);
        x/=10;
    }

    return num;
}

ll getFactor(ll x) {
    if(x <= lim) {
        if(criba[x]) return criba[x];
    }
    else {
        for(int i=0;i<np;i++)
            if(x%primes[i] == 0)
                return primes[i];
    }
    return 1;
}

void tryN(ll N) {
    ll res[15];

    for(ll i = 2;i<=10;i++) {
        ll num = toBin(N);
        num = toBase(num,i);


        ll factor = getFactor(num);

        if(factor == 1)
            return;
        res[i] = factor;
    }

    printf("%llu>",j);

    fprintf(out,"%llu",toBin(N));

    for(ll i = 2;i<=10;i++) {
        fprintf(out," %llu",res[i]);
    }
    fprintf(out,"\n");
    j--;
}

int main() {
    for(ll i=2;i<=lim;i++) {
        if(!criba[i]) {
            primes[np++] = i;
            for(ll j=i+i;j<=lim;j+=i)
                criba[j] = i;
        }
    }

    in = fopen("input.in", "r");
    out = fopen("output.out", "w+");

    fscanf(in,"%llu",&t);

    for(ll k=1;k<=t;k++) {
        fprintf(out,"Case #%llu:\n",k);

        while(j) {
            tryN(n);
            n += 2;
        }
    }

    return 0;
}

