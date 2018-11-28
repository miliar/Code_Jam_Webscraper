#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define INF 0x3f3f3f3f
#define MAX 10000
#define pi 3.1415926

using namespace std;
long long int T,r,t;


int main(){
#ifndef ONLINE_JUDGE
    freopen("G:\\study\\programs\\test\\in.txt","r",stdin);
    freopen("G:\\study\\programs\\test\\out.txt","w",stdout);
#endif
    long long int cases;
    long long int num;
    int r1,r2;
    scanf("%lld",&T);
    for(cases = 0;cases < T;++ cases){
        scanf("%lld %lld",&r,&t);
        num = 0;
        r2 = r +1,r1 = r;
        while(t >= r2 * r2 - r1 * r1){
            //printf("%lld\n",t);
            t -= r2 * r2 - r1 * r1;
            num ++;
            r2 += 2, r1 += 2;
        }
        printf("Case #%lld: %lld\n",cases + 1,num);
    }
    return 0;
}
