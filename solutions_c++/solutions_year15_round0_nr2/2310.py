#include<iostream>
#include<map>
#include<iterator>
#include<climits>
using namespace std;
int main(){
	int t,cas,ans,stp,tmp,n;
	cin>>t;
	cas=0;
	while(t--){
		cas++;
		cin>>n;
		int arr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		ans= INT_MAX;
		for(int i=1;i<=1000;i++){
			tmp=0;
			for(int j=0;j<n;j++){
				if(arr[j]<i)
					continue;
				if(arr[j]%i==0)
					tmp+=((arr[j]/i)-1);
				else tmp+=(arr[j]/i);
			}
			tmp+=i;
			ans=min(ans,tmp);
		}
		cout<<"Case #"<<cas<<": "<<ans<<"\n";
	}
}


