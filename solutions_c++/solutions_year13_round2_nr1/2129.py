/*
ID: ankitgu1
LANG: C++
TASK: holstein
*/
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in,*out;

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

typedef long long LL;
typedef long L;

int is_prime(long long num) {
    for(long long t=2; t<=sqrt(num); t++) {
        if(num%t==0)return 0;
    }
    return 1;
}
LL gcd(LL a,LL b) {
    if(a%b==0)return b;
    return gcd(b,a%b);
}
int compare (const void * a, const void * b) {
    return ( *(int*)a - *(int*)b );
}
int dec_compare (const void * a, const void * b) {
    return ( - *(int*)a + *(int*)b );
}
//////////////////////////

#define DEBUG 1

int arr[200];
int mem[200];

LL n;

LL solve(LL value,int a){
    //cout<<"what "<<value<<" "<<a<<endl;
    if(a>=n)return 0;
    else if(value > arr[a]){
        value +=arr[a];
        return solve(value,a+1);
    }LL ans=100000000;
    if(value>1)ans = solve(2*value-1,a);
    ans = MIN(ans , solve(value,a+1));
    return (ans+1);
}

int main() {
    in=fopen("input.in","r");
    out=fopen("output.out","w");
    int cases;
    fscanf(in,"%d",&cases);
    for(int test=0;test<cases;test++){
        fprintf(out,"Case #%d: ",test+1);

        memset(arr,0,sizeof(arr));
        LL val;
        fscanf(in,"%lld %lld",&val,&n);

        for(int t=0;t<n;t++)
        fscanf(in,"%d",&arr[t]);

        qsort(arr,n,sizeof(int),compare);

        fprintf(out,"%lld\n",solve(val,0));
    }
    fclose(in);
    fclose(out);
    return 0;
}
