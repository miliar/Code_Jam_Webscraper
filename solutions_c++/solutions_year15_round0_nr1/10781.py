#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	int t,i,k,j,l,max,temp,et;
	char jk;
	cin>>t;
	int extra=0;
	for(int l=0;l<t;l++) {
		extra=temp=0;
		cin>>max;
		cin>>jk;
		temp = jk - '0';
		for(int i=1;i<=max;i++) {
			cin>>jk;
			j = jk - '0';
		//	cout<<"value :"<<j<<endl;
			et = i-temp > 0 ? i-temp : 0;
			extra += et;
		//	cout<<"extra:"<<extra<<endl;
			temp += j+ et;
		}
		cout<<"Case #"<<l+1<<": "<<extra<<endl;
	}
	return 0;
}
