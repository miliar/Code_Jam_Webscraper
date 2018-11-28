#include<bits/stdc++.h>

using namespace std;

int main()
{
	long long int T, N, a[1003], temp, ans1, ans2;
	cin>>T;
	for(long long int t=1;t<=T;t++)
	{
		ans1=0;
		ans2=0;
		temp=-100000000;
		cin>>N;
		for(long long int i=0;i<N;i++)
			cin>>a[i];
		for(long long int i=0;i<N-1;i++)
			if(a[i+1]<a[i])
				ans1+=(a[i]-a[i+1]);
		for(long long int i=0;i<N-1;i++)
				temp=max(temp,a[i]-a[i+1]);
		if(temp<=0)
			ans2=0;
		else
			for(long long int i=0;i<N-1;i++)
			{
				if(a[i]>a[i+1] && a[i+1]!=0)
					ans2+=min(temp,a[i]);
				else if(a[i]>a[i+1] && a[i+1]==0)
					ans2+=(a[i]-a[i+1]);
				else if(a[i]==0 && a[i+1]==0)
					;
				else if(a[i]<=a[i+1])
					ans2+=min(temp,a[i]);
			}
		cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}