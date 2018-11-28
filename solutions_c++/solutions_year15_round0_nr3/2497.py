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
int dp[200][200];
int total[10000+10];
char arr[10000+10] , A[10000+10];
void pre_process()
{
    dp[1][1] = 1 ; dp[1]['i'] = 'i' ; dp[1]['j'] = 'j' ; dp[1]['k'] = 'k' ;
    dp['i'][1] = 1 ; dp['i']['i'] = -1 ; dp['i']['j'] = 'k' ; dp['i']['k'] = -'j' ;
    dp['j'][1] = 'j' ; dp['j']['i'] = -'k' ; dp['j']['j'] = -1 ; dp['j']['k'] = 'i' ;
    dp['k'][1] = 'k' ; dp['k']['i'] = 'j' ; dp['k']['j'] = -'i' ; dp['k']['k'] = -1 ;
}
int multiplexing(int t,int y)
{
    if(y<0) return -dp[-y][t];
    return dp[y][t];
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    pre_process();
    int T ;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int L , X , cnt = 0 ;
        scanf("%d%d%s",&L,&X,arr);
        memo(A,NULL);
        for(int i=1;i<=X;i++)
        {
            for(int j=0;j<L;j++) A[cnt++] = arr[j] ;
        }
        for(int i=0;i<cnt;i++)
        {
            int prev = 1 ;
            for(int j=i;j<cnt;j++)
            {
                prev = multiplexing(A[j],prev);
            }
            total[i] = prev ;
        }
        int prev = 1 ;
        bool flag = false ;
        for(int i=0;i<cnt;i++)
        {
            prev = multiplexing(A[i],prev);
            if(prev=='i')
            {
                int jprev = 1 ;
                for(int j=i+1;j<cnt-1;j++)
                {
                    jprev = multiplexing(A[j],jprev);
                    if(jprev=='j'&&total[j+1]=='k') flag = true ;
                }
            }
        }
        if(flag) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);
    }
    return 0;
}
