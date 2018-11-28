typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair

using namespace std;
ll mark[100007],val[100007];
int main()
{
    ll t,i,maxi=2501,n,j,x,w=1;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        memset(mark,0,sizeof(mark));
        memset(val,0,sizeof(val));
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%lld",&x);
                mark[x]=1;
                val[x]++;
            }
        }
        printf("Case #%lld: ",w++);
        for(i=1;i<=maxi;i++)
        {
            if(mark[i]==1 && val[i]%2!=0)
            printf("%lld ",i);
        }
        printf("\n");
    }
	return 0;
}