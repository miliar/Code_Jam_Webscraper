#include <bits/stdc++.h>
#define ll long long int

using namespace std;
ll arr[10000];

int main()
{
	ios_base::sync_with_stdio(false);
	ll t;
	cin>>t;

	for(int h=1; h<=t ; h++)
	{
		ll n;
		cin>>n;
		cin.ignore();
		string s="";

		for(int l=0 ; l<=n ; l++)
		{
			arr[l]=0;
		}
		
		cin>>s;

		ll size = s.size();

		for(int i =0 ; i<size; i++)
		{
			arr[i]=(int)s[i]-48;
		} 

		ll ans=0;
		ll sum=0;
		if(arr[0]==0)
		{
			ans++;
			sum=1;
		}
		else
		{
			ans = 0;
			sum = arr[0];
		}
			

		for(int l=1 ; l<=n ; l++)
		{
			if(sum>=l)
			{
				sum += arr[l];
			}
			else
			{
				ans += (l-sum);
				sum += (l-sum);
				sum += arr[l];
			}
			
		}


		cout<<"Case #"<<h<<": "<<ans<<endl;



	}


}