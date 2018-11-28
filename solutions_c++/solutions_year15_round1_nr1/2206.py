#include<bits/stdc++.h>

using namespace std;
int arr[10005];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
	{
    	
    	int sol1=0,sol2=0,maxx=0;

        int n;
        cin>>n;
        for(int i=0;i<n;i++)
		{
        	
            cin>>arr[i];
        }
        for(int i=1;i<n;i++)
		{
        	
            if(arr[i]-arr[i-1]<0)
			{
                sol1+=(arr[i-1]-arr[i]);
            }
            maxx=max(maxx,arr[i-1]-arr[i]);
        }
        for(int i=0;i<n-1;i++)
		{
            if(arr[i]>=maxx)
			sol2+=maxx;
            else 
			sol2+=arr[i];
        }
        printf("Case #%d: %d %d\n",z,sol1,sol2);

    }
    return 0;
}
