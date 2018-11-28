#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<math.h>
#include<climits>
#include<time.h>
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
    #endif
    //clock_t start=clock();
    int t;
    double c, f, x, ans, temp, prev, curr;
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        scanf("%lf%lf%lf", &c,&f,&x);
        ans=x/2.0;
        prev=ans;
        temp=0;
        for(int i=1; ; i++)
        {
            temp+=c/(2.0+(i-1)*f);
            curr=temp+(x/(2.0+i*f));
            ans=min(ans, curr);
            if(curr>prev)
                break;
            prev=curr;
        }
        printf("Case #%d: %.7lf\n", cas,ans);
    }

    //while (clock() - start < (0.98) * CLOCKS_PER_SEC);
    return 0;
}
