#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n;
		cin>>n;
		double num1[n],num2[n];
		for(int q=0;q<n;q++){
			cin>>num1[q];
		}
		for(int q=0;q<n;q++){
			cin>>num2[q];
		}
		sort(num1,num1+n);
		sort(num2,num2+n);
		int out1=0,out2=0;
		int cnt=n-1;
		for(int q=n-1;q>=0;q--){
			if(num1[cnt]>num2[q]){
				cnt--;
				out1++;
			}
		}
		cnt=n-1;
		for(int q=n-1;q>=0;q--){
			if(num1[q]>num2[cnt]){
				out2++;
			}
			else{
				cnt--;
			}
		}
		cout<<"Case #"<<i<<": "<<out1<<" "<<out2<<endl;
	}
	return 0;
}
