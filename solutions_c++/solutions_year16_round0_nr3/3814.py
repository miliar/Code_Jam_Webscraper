// Author : Muhammad Rifayat Samee
// Problem : C
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
i64 n,k,w;
i64 isprime(i64 n){
    i64 i,k;
    //printf("i am here %lld\n",n);
    if(n==1)return 0;
    if(n==2)return 1;
    if(n%2==0){
        w = 2;
        return 0;
    }
    k = sqrt(n);
    for(i=3;i<=k;i++){
        if(n%i==0){
            w = i;
            return 0;
        }
    }
    return 1;
}
i64 number_in_base(i64 n,i64 b){
    i64 r,res,rr;
    res = 0;
    rr = 1;
    while(n!=0){
        r = n%2;
        res = res + rr*r;
        rr = rr * b;
        n = n/2;
    }
    return res;
}
void printbin(i64 n){
    i64 i;
    for(i=15;i>=0;i--){
        if(n&((i64)1<<i))printf("1");
        else
            printf("0");
    }
    //printf("\n");
}
int main(){

	//freopen("in.txt","r",stdin);
	freopen("C1.out","w",stdout);
	i64 i,j,k,ct=1;
	i64 res = 0;
	printf("Case #%lld:\n",ct);
	for(i=(1<<15)+1;;i=i+2){
        for(j=2;j<=10;j++){
            if(isprime(number_in_base(i,j))){
                break;
            }
        }
        if(j==11){
            res++;
            //printf("?? %lld ",number_in_base(i,8));
            printbin(i);
            for(k=2;k<=10;k++){
                isprime(number_in_base(i,k));
                printf(" %lld",w);
            }
            printf("\n");
            //printf("%d\n",res);
        }
        if(res == 50)break;
    }

	return 0;
}
