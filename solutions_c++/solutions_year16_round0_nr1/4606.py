#include <iostream>
#include <vector>

using namespace std;

int found = 0;
int out;
vector<bool> nums(10,false);

void findnr(int n){
	if(n>=10){
		findnr(n/10);
	}
	if(!nums[n%10]){
		nums[n%10]=true;
		found++;
	}
}

int main(){
	int n,curr,t;
	cin>>t;
	for(int i=0;i<t;i++){
		found = 0;
		curr=1;
		fill(nums.begin(),nums.end(),0);
		cin>>n;
		if(n==0){
			found=10;
		}
		while(found<10){
			findnr(curr*n);
			curr++;
		}
		if(n==0){
			cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
		}
		else{
			cout<<"Case #"<<i+1<<": "<<(curr-1)*n<<"\n";
		}
	}
	return 0;
}