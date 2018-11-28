#include<bits/stdc++.h>

using namespace std;
#define ll long long


int main()
{
	ll t,n;
	ifstream myfile ("input1l.in");
	ofstream outfile("ans1l.txt");
	myfile>>t;
	for(ll test=1;test<=t;test++)
	{
		myfile>>n;
		ll i=1, ans=0;
		ll arr[10]={0};
		ll flag1=0;
		while(1)
		{
			if(n==0)
			{
				flag1=1;
				break;
			}
			ll chk = (i++)*n;
			ans = chk;

			while(chk)
			{
				arr[chk%10]++;
				chk/=10;
			}
			int flag=0;
			for(int j=0;j<=9;j++)
			{
				if(arr[j]==0)
					flag=1;
			}
			if(flag==0)
				break;
		}
		if(flag1)
		{
			outfile<<"Case #"<<test<<": INSOMNIA"<<endl;
		}
		else
		{
			outfile<<"Case #"<<test<<": "<<ans<<endl;
		}


	}


	return 0;
}
