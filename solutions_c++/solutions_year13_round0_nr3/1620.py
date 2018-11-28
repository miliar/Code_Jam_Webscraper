#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

long long br[1555111];

bool palin(long long x) {

    int p,i,b,a[25];

    p=0;
    while(x) {
        a[p++]=x%10;
        x/=10;
    }

    b=1;
    for(i=0; i+i<p; i++) {
        if(a[i]!=a[p-1-i]) b=0;
    }

    return b;
}

int main() {

    FILE *ff=fopen("C-large-1.in", "r"), *gg=fopen("C-large-1.out", "w");

    int k,ka,kb,tt,ttt;
    long long i,a,b;

    k=0;
    for(i=1; i<=10000000; i++) {
        if (palin(i) && palin(i*i)) br[k++] = i*i;
    }

    //printf("%d\n", k);
    //for(i=0; i<k; i++) printf("%lldLL, ", br[i]);

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%lld %lld", &a, &b);

        kb=0; ka=0;
        while(kb < k && br[kb] <= b) kb++;
        while(ka < k && br[ka] < a) ka++;

        fprintf(gg,"Case #%d: %d\n", tt, kb-ka);
    }

    fclose(ff); fclose(gg);

    return 0;
}
