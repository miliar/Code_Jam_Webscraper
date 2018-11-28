#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
   
	int t,i,j,n,tt;
	double ken[2000],naomi[2000];
	cin>>t;
	for(tt=1;tt<=t;tt++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>naomi[i];
        for(i=0;i<n;i++)
            cin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int var1=0,var2=0;
        i=0,j=0;
        while(i<n&&j<n)
        {
            if(naomi[i]>ken[j])
            {
                var1++;
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
                var2++;
                i++;
                j++;
            }
            else
                j++;
        }
        printf("Case #%d: %d %d\n",tt,var1,n-var2);
    }

	return 0;
}
