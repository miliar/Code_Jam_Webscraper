#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		
		int n;
		cin>>n;
		int ar[n+1];
		for(int i=0;i<n;i++)
		cin>>ar[i];
		int ans1=0,ans2=0,mx=0;
		for(int i=1;i<n;i++)
		{
			if(ar[i]<ar[i-1])
			ans1+=ar[i-1]-ar[i];
            mx=max(mx,ar[i-1]-ar[i]);
		//ans2+=ar[i];
		}
      for(int i=0;i<n-1;i++)
		ans2+=min(ar[i],mx);
		//ans2-=abs(ar[0]-ar[n-1]);
		
		cout<<"Case #"<<c<<": "<<ans1<<"\t"<<ans2<<endl;
	}
	
	return 0;
}