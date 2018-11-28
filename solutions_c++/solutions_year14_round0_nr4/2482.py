#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MST(a,b) memset(a,b,sizeof(a))
#define MAXN    1050
double  A[MAXN],B[MAXN];
int n;
int cover()
{
    int ans=0,j=n;
    for(int i=n;i>=1;i--)
    {
        while(j>=1 && B[i]<A[j])j--;
        if(j<1)break;
        ans++;
        j--;
    }
    return ans;
}
int cover2()
{
    int ans=0,j=1;
    for(int i=1;i<=n;i++)
    {
        while(j<=n && B[i]>A[j])j++;
        if(j>n)break;
        ans++;
        j++;
    }
    return ans;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int nn;
    scanf("%d",&nn);
    FOR(ii,1,nn)
    {
        scanf("%d",&n);
        int ans1,ans2;
        FOR(i,1,n)scanf("%lf",&A[i]);
        FOR(i,1,n)scanf("%lf",&B[i]);
        sort(A+1,A+n+1);
        sort(B+1,B+n+1);
        /*FOR(i,1,n)printf("%lf ",A[i]);
        printf("\n");
        FOR(i,1,n)printf("%lf ",B[i]);
        printf("\n");*/
        ans1=cover2();
        ans2=n-cover();
        printf("Case #%d: %d %d\n",ii,ans1,ans2);
    }
    return 0;
}
