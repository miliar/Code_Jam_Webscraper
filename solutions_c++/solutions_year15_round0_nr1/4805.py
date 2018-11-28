#include<iostream>
#include<string>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int k;
		cin>>k;
		string num;
		cin>>num;
		int ans=0;
		int sum=0;
		for(int j=0;j<=k;j++){
			if(sum<j){
				ans+=(j-sum);
				sum+=j-sum;
			}
			sum+=(num[j]-'0');
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}
