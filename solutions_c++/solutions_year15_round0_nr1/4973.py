#include<bits/stdc++.h>

using namespace std;

int main(){
	int test;
	cin>>test;
	for(int te=0;te<test;te++){
		int maxShy;
		cin>>maxShy;
		string shy;
		cin>>shy;

		int res = 0;
		int tempsum = 0;

		for(int i=0;i<=maxShy;i++){
			if(i==0){
				tempsum += shy[i] - '0';
				continue;
			}
			if(i > tempsum && shy[i]!='0'){
				res += i - tempsum;
				tempsum +=  res;
			}
			tempsum += shy[i] - '0';
		}
		cout<<"Case #"<<(te+1)<<": "<<res<<endl;
	}

	return 0;
}