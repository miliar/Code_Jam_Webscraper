#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(v,x) v.push_back(x)
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
int a[200][200];
int main()
{
    FILE *fp1;FILE *fp2;
    fp1 = fopen("input.txt","r");
    fp2 = fopen("output.txt","w");
    int t;
    ll n,i,j;
    fscanf(fp1,"%d",&t);
    for(int test=1;test<=t;test++)
    {
        fscanf(fp1,"%d",&n);
        int f[2501];
        memset(f,0,sizeof(f));
        REP(i,2*n-1) REP(j,n) fscanf(fp1,"%d",&a[i][j]);
        REP(i,2*n-1) REP(j,n) f[a[i][j]]++;
        fprintf(fp2,"Case #%d: ",test);
        REP(i,2501) if(f[i]%2) fprintf(fp2,"%d ",i);
        fprintf(fp2,"\n");

    }
    return 0;
}
