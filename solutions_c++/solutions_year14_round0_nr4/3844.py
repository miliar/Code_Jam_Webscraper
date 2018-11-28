#include <iostream>
#include <algorithm>
#include <cstring>
#include <utility>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define for1(i,n) for(i=0;i<n;i++)
#define for2(i,n) for(i=1;i<=n;i++)
#define all(v) v.begin(),v.end()
#define set(a,b) memset(a,b,sizeof a)
#define cin3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define cin2(a,b) scanf("%d%d",&a,&b)
#define cin1(a) scanf("%d",&a)
#define pb push_back
#define mp make_pair
#define inf  1e8


int main()
{
    int i,j,k,l,loop,n,ind2,rslt,ind1;
    float ar1[1010],ar2[1010];

    cin1(loop);
    for2(l,loop)
    {
        cin1(n);
        for1(i,n)
        {
            cin>>ar1[i];
        }
        for1(i,n)
        {
            cin>>ar2[i];
        }
        sort(ar1,ar1+n);
        sort(ar2,ar2+n);
        ind1=ind2=0;
        for(i=0,j=n-1,k=n-1;i<n;i++)
        {
            if(ar1[i]<ar2[ind1])
            {
                j--;
            }
            else
            {
                ind1++;
            }
            if(ar2[i]<ar1[ind2])
            {
                k--;
            }
            else
            {
                ind2++;
            }
            if(ind1>j || ind2>k)
            {
                break;
            }
        }
        ind2=n-ind2;
        printf("Case #%d: %d %d\n",l,ind1,ind2);
    }
    return 0;
}
