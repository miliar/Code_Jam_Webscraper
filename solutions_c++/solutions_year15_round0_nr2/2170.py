#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int _,n,T,A[1005],ans,sum,i,j;
int main()
{
    scanf("%d",&T);
    for (_=1; _<=T; _++)
    {
        scanf("%d",&n);
        for (i=1; i<=n; i++) scanf("%d",&A[i]);
        ans=1000;
        for (i=1; i<=1000; i++)
        {
            sum=0;
            for (j=1; j<=n; j++) sum+=(A[j]-1)/i;
            ans=min(ans,i+sum);
        }
        cout<<"Case #"<<_<<": "<<ans<<endl;
    }
    return 0;
}
