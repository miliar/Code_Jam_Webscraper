#include <iostream>
#include <stack>

using namespace std;

int main(){
	int T,N,nr,next;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>N>>nr;
		stack<int> nums;
		
		while(nr>0){
			nums.push(nr%10);
			nr /= 10;
		}
		for(int j=0;j<nums.size()-(N+1);j++){
			nums.push(0);
		}

		int sum=0;
		int res=0;
		for(int j=0;j<N+1;j++){
			next = nums.top();
			//cout<<j<<"--"<<sum<<"--"<<next<<endl;
			if(j>sum){
				//cout<<"looool"<<endl;
				res+=j-sum;
				sum+=j-sum;
			}
			sum+=next;
			nums.pop();
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}