/*
    Author : RAJON BARDHAN
    AUST CSE 27th Batch
    All my programming success are dedicated to my love TANIA SULTANA RIMY

    ALGORITHM : AD HOC
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
vector <int> coin ;
int C , D , V ;
bool make(int target,int index,int far)
{
    if(far==target) return true ;
    if(far>target) return false ;
    if(index==coin.size()) return false ;
    if(make(target,index+1,far)) return true ;
    if(make(target,index+1,far+coin[index])) return true ;
    return false ;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T ;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        coin.clear();
        scanf("%d%d%d",&C,&D,&V);
        for(int i=0;i<D;i++)
        {
            int a ;
            scanf("%d",&a);
            coin.pb(a);
        }
        int ans = 0 ;
        for(int i=1;i<=V;i++)
        {
            if(make(i,0,0)) continue ;
            ans++;
            coin.pb(i);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
