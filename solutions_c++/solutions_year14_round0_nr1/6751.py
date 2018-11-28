#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
#include<climits>
#include<set>
#include<cmath>
#include<bitset>
#include<map>
#include<iostream>
#include<queue>
#define test(t) while(t--)
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define p(n) printf("%d\n",n)
#define rep(i,a,n) for(i=a;i<=n;i++)
#define vi vector<int>
#define vii vector< vector<int> >
#define vpii vector< pair<int,int> >
#define mii map<int,int>
#define pb push_back
#define inf 1000000000LL
#define mp make_pair
#define imax 1000000000
//#define inf 100000000
#define ll long long
using namespace std;
main()
{
int t;
int ar[5][5];
int n;
int temp[5];
int ans;
int cnt;
s(t);
int z = 0;
while(++z <= t)
{
    s(n);
    for(int i = 1; i < 5; i++)
        for(int j = 1; j < 5; j++)
        s(ar[i][j]);
//printf("%d  \n",n);
    for(int i = 1; i < 5; i++)
        temp[i] = ar[n][i];
    s(n);
/*for(int i = 1; i < 5; i++)
       {
        for(int j = 1; j < 5; j++)
        printf("%d  ",ar[i][j]);
        printf("\n");
       }*/

    for(int i = 1; i < 5; i++)
        for(int j = 1; j < 5; j++)
        s(ar[i][j]);
       /* printf("%d  \n",n);
        for(int i = 1; i < 5; i++)
       {
        for(int j = 1; j < 5; j++)
        printf("%d  ",ar[i][j]);
        printf("\n");
       }*/
    cnt = 0;
    for(int j = 1; j < 5; j++)
    for(int i = 1; i < 5; i++)
    {
        if(temp[j] == ar[n][i])
        {
            ans = temp[j];
            cnt++;
        }
    }


    if(!cnt)
    {printf("Case #%d: Volunteer cheated!\n",z);}
    else if(cnt > 1)
     {printf("Case #%d: Bad magician!\n",z);}
    else
     {
        printf("Case #%d: %d\n",z,ans);
     }


}

return 0;
}
