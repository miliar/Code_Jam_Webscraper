/*
    Author : RAJON BARDHAN
    AUST CSE 27th Batch
    All my programming success are dedicated to my love TANIA SULTANA RIMY

    ALGORITHM : Brute Force
*/
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define ff first
#define ss second
#define memo(a,b) memset(a,b,sizeof(a))
#define EPS 1e-8
#define PI 3.14159265358979323846
typedef long long ll ;
int A[100],B[100],D;
bool valid(int khabe,int interval)
{
    for(int i=1;i<=D;i++) B[i] = A[i] ;
    while(interval--)
    {
        sort(&B[1],&B[D+1]);
        if(B[D]-khabe>=0) B[D]-=khabe;
    }
    for(int i=1;i<=D;i++)
    {
        if(B[i]>khabe) return false ;
    }
    return true ;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T ;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int ans = INT_MAX ;
        cin >> D ;
        for(int i=1;i<=D;i++) cin >> A[i] ;
        sort(&A[1],&A[D+1]);
        for(int i=1;i<=9;i++)
        {
            for(int j=0;j<=9;j++)
            {
                if(valid(i,j)) ans=min(ans,i+j);
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
