#include <iostream>
using namespace std;

int main() {
	int cases,smax,friends,sp,c=1;
	string s;
	cin>>cases;
	while(cases--){
		friends=0;
		cin>>smax>>s;
		sp=s[0]-'0';
		for(int i=1;i<s.length();i++){
			if((s[i]-'0') > 0){
				if(sp<i)
					friends+=i-sp;
					sp+=friends;
			} 
			sp+=s[i]-'0';
			
		}
		cout<<"Case #"<<c<<": "<<friends<<endl;
		c++;
	}
	return 0;
}