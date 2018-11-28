#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long

int main()
{
    in("in.txt");
    out("out.txt");
    long long int t,n,caseno=1;
    scanf("%lld",&t);
    while(t--){
        scanf("%lld",&n);
        long long int ar[100];
        long long int cnt=10;
        long long int current=n;
        long long int counter=1;
        memset(ar,0,sizeof(ar));
        long long int val;
        long long int somnia=0;
        while(cnt>0){
            long long int x=current*counter;
            val=x;
            while(x){
                long long int dig=x%10;
                if(ar[dig]==0){
                    ar[dig]=1;
                    cnt--;
                }
                x/=10;
            }
            if(val==0){
                somnia=true;
                break;
            }
            if(cnt==0)break;
//            cout<<x<<" "<<current<<" "<<counter<<endl;
            counter++;
        }
        if(somnia){
            printf("Case #%lld: INSOMNIA\n",caseno++);
        }
        else
            printf("Case #%lld: %lld\n",caseno++,val);
    }
    return 0;
}
