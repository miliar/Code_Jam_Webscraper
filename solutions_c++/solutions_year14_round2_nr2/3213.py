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
    int *ar = (int *)malloc(sizeof(int) * 1000*1000);
    for(int i = 0; i < 1000; i++)
        for(int j = 0; j < 1000; j++)
        ar[i * 1000 + j] = i&j;


    int t;
    int a, k, b;
    scanf("%d",&t);
    long long int ans ;
    for(int q = 1; q <= t; q++)
    {
        ans = 0;
        scanf("%d%d%d",&a,&b,&k);
        for(int i = 0; i < a; i++)
            for(int j = 0; j < b; j++)
            if(ar[i*1000+j] < k)
            ans++;
        printf("Case #%d: %lld\n",q,ans);
    }

return 0;
}
