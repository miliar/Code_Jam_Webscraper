#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in", "rt", stdin);
    freopen("D-large0.out", "wt", stdout);
	int t,i,j,n,k;
	double ken[2000],naomi[2000];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>naomi[i];
        for(i=0;i<n;i++)
            cin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int d_war=0,war=0;
        i=0,j=0;
        while(i<n&&j<n)
        {
            if(naomi[i]>ken[j])
            {
                d_war++;
                i++;
                j++;
            }
            else
                i++;
        }
        i=0,j=0;
        while(i<n&&j<n)
        {
            if(naomi[i]<ken[j])
            {
                war++;
                i++;
                j++;
            }
            else
                j++;
        }
        printf("Case #%d: %d %d\n",k,d_war,n-war);
    }

	return 0;
}
