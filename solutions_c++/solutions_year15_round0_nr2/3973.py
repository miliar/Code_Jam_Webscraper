#include <bits/stdc++.h>
using namespace std;

int main()
{
    
int t;
cin>>t;
int o=1;
while(o<=t)
{
		long int d;
		cin>>d;
		long int maxi=0;
		long int arr[1000]={0};
		for(long int i=0;i<d;i++)
			{cin>>arr[i];if(arr[i]>maxi)maxi=arr[i];}
			long int ans=LONG_MAX;
		for(long int i=1;i<maxi;i++)
		{
			long int tim=0;
			for(long int j=0;j<d;j++)
			{
				tim+=(arr[j]-1)/i;
			}
			tim+=i;
			if(tim<ans)ans=tim;
		}
		if(ans>maxi)ans=maxi;
		cout<<"Case #"<<o<<": "<<ans;
		if(o!=t)cout<<endl;
o++;
}

return 0;
}
