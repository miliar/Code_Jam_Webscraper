#include<bits/stdc++.h>

#define xx first
#define yy second
#define LL long long
#define inf 100000000
#define pb push_back
#define vsort(v) sort(v.begin(),v.end())
#define pi acos(-1)
#define clr(a,b) memset(a,b,sizeof a)
#define bclr(a) memset(a,false,sizeof a)
#define pii pair<int,int>
#define MOD 1000000007
#define MP make_pair
#define MX 1005

using namespace std;

int solve(int x){
    int bit=0;
    for(int i=1;;i++){
        int xx=x*i;
        while(xx>0){
            int d=xx%10;
            xx/=10;
            bit|=(1<<d);
        }
        if(bit==1023) return x*i;
    }
}

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test; scanf("%d",&test);
    for(int kase=1;kase<=test;kase++){
        int n; scanf("%d",&n);
        printf("Case #%d: ",kase);
        if(n==0) puts("INSOMNIA");
        else printf("%d\n",solve(n));
    }
    return 0;
}

