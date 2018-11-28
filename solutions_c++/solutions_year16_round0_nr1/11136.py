#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<climits>
#include<map>
#include<math.h>
#include<algorithm>
#define LL long long int
#define P(N) printf("%d\n",N);
#define S(N) scanf("%d",&N);
#define SL(N) scanf("%lld",&N);
#define pb push_back
#define mp make_pair
#define pnl printf("\n");
#define FOR(i,a,b) for (i=a;i<=b;i++)
#define mem(a,val) memset(a,val,sizeof(a))
using namespace std;
int gcd(int a, int b){ int temp; while(b>0) { temp= b; b=a%b; a=temp;}  return a;}
bool ar[11];

bool check(LL x, LL N) {
    LL num = x*N;
    if(num==0) ar[0] = true;
    while(num) {
        ar[num%10]= true;
        num/=10;
    }
    for(int i=0;i<10;i++) {
        if(ar[i]==false)
            return false;
    }
    return true;
}
int main()
{
    int t;
    S(t);
    for(int i=1;i<=t;i++)
    {
        LL N;
        cin>>N;
        LL x = 1;
        memset(ar, false, sizeof(ar));
        while(x<1000000) {
            if(check(x,N)) {
                break;
            }
            x++;
        }
        if(x==1000000) {
            printf("Case #%d: INSOMNIA\n",i);
        } else {
            printf("Case #%d: %lld\n",i,x*N);
        }
    }
return 0;
}
