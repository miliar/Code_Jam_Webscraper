#include<iostream>
#include<vector>
using namespace std;
int main(){
	int t,ith=1;
	cin>>t;
	while(t--){
		int n;
		int data;
		cin>>n;
		vector<int> v;
		getchar();
		for(int i=0;i<=n;i++){
			data=getchar();
			data-=48;
			v.push_back(data);
		}
		int sum=0, required=0;
		for(int i=1;i<=n;i++){
			sum+=v[i-1];
			if(v[i]!=0){
				if(sum<i){
					required+=i-sum;
					sum+=(i-sum);
				}
			}	
		}
		cout<<"Case #"<<ith++<<": "<<required<<endl;
	}

	return 0;
}