#include <bits/stdc++.h>

using namespace std;

int main(){
	
	int t,n,a[1010];

	cin>>t;

	for(int j=1;j<=t;j++){

		cin>>n;

		for(int i=0;i<n;i++)
			cin>>a[i];

		int first=0,second=0,rate=0;

		int diff[1010];

		for(int i=0;i<n-1;i++)
			diff[i]=a[i]-a[i+1];

		for(int i=0;i<n-1;i++){
			if(diff[i]>rate)
				rate=diff[i];
		}

		for(int i=0;i<n-1;i++){

			if(a[i+1]<a[i])
				first+=a[i]-a[i+1];
		}

		for(int i=0;i<n-1;i++){

				second+=min(rate,a[i]);
		}	

		cout<<"Case #"<<j<<": "<<first<<" "<<second<<endl;
	}

	return 0;

}
