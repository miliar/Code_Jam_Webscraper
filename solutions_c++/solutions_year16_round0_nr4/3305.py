#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(v,x) v.push_back(x)
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
int main()
{
    FILE *fp1;FILE *fp2;
    fp1 = fopen("input.txt","r");
    fp2 = fopen("output.txt","w");
    int t;
    ll n,k,c,s,i;
    fscanf(fp1,"%d",&t);
    for(int test=1;test<=t;test++)
    {
        fscanf(fp1,"%lld%lld%lld",&k,&c,&s);
        fprintf(fp2,"Case #%d: ",test);
        ll x = pow(k,c-1);
        REP(i,k) fprintf(fp2,"%lld ",1 + i*x);
        fprintf(fp2,"\n");
    }
    return 0;
}
