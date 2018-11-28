#include <vector>
#include <string>
#include<fstream>
#include<stdio.h>

using namespace std;


int main()
{
    //freopen("practice.in","r",stdin);
	freopen("A-large.in","r",stdin);
	//freopen("C-large-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	long long test,q;
	scanf("%lld",&test);
	for(q=1;q<=test;q++)
    {
        long long arr[100002],i,j,n;
        long long val1,val2,maxi,left;
        scanf("%lld",&n);
        for(i=0;i<n;i++)
            scanf("%lld",&arr[i]);
        val1=0;maxi=0;
        for(i=0;i<n-1;i++)
        {
            if(arr[i]-arr[i+1]>0)
                val1+=(arr[i]-arr[i+1]);
            if(arr[i]-arr[i+1]>maxi)
                maxi=(arr[i]-arr[i+1]);
        }
        val2=0;left=0;
        for(i=0;i<n-1;i++)
        {
            left=arr[i];
            if(left>=maxi)
            {
                //left-=maxi;
                val2+=maxi;
            }
            else if(left>0)
            {
                val2+=left;
                //left=0;
            }
        }
        printf("Case #%lld: ",q);
        printf("%lld %lld\n",val1,val2);
    }

	return 0;
}


