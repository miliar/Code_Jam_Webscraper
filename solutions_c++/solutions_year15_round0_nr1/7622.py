#include <iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	int T, a, sum, add;
	string s;
	cin>>T;
	for(int t=1; t<=T; t++){
		cin>>a>>s;
		sum=add=0;
		for(int i=0; i<=a; i++){
			if(sum<i){
				add+=i-sum;
				sum+=i-sum;
			}
			sum+=s[i]-'0';
		}
		cout<<"Case #"<<t<<": "<<add<<"\n";
	}
	
	return 0;
}
