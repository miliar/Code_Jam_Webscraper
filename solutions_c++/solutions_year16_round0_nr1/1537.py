#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll solve(ll n)
{
    if(n==0){
        return -1;
    }
    int A[11], k=2;
    ll num=n;
    memset(A, 0, sizeof A);
    while(1){
        ll m=n;
        while(m){
            A[m%10]=1;
            m/=10;
        }
        int f=1;
        for(int i=0; i<=9; i++){
            if(A[i]==0){
                f=0;
                break;
            }
        }
        if(f){
            return n;
        }
        n=num*k;
        k++;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    ll n;
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        scanf("%lld", &n);
        ll ans = solve(n);
        if(ans==-1)
            printf("Case #%d: INSOMNIA\n", i);
        else
            printf("Case #%d: %lld\n", i, ans);
    }
    return 0;
}
