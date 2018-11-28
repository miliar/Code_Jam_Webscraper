#include<iostream>

using namespace std;

bool done(int *nums){
	for(int i=0;i<10;i++){
		if(nums[i] == 0){
			return false;
		}
	}
	
	return true;
}

int main(){
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++){
		int nums[10] = {0};
		
		long n;
		cin>>n;
		
		if(n == 0){
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		
		long m = n;
		
		int multiplier  = 1;
		
		while(!done(nums)){
			int temp = n;
			
			while(temp>=1){
				nums[(int)(temp%10)] = 1;
				temp/=10;
				
				//for(int j=0;j<10;j++){
			//		cout<<nums[j]<<" ";
			//	}
			//	cout<<"\n";
			}
			
			multiplier++;
			n=m*multiplier;
		}
		
		cout<<"Case #"<<i+1<<": "<<n-m<<"\n";
		
		
	}
}
