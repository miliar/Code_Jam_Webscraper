#include<iostream>

using namespace std;

int main()
{
	int t,k,i,sum;
	cin>>t;
	string s;
	int count,n;
	for(k=1;k<=t;k++) {
		cin>>n;
		char ch;
	//	cin>>ch;
		s ="";
		cin>>s;
//		cout<<s<<endl;
		sum = s[0]-48;
	//	cout<<sum<<endl;
		count = 0;
		for(i=1;i<s.length();i++) {
			if(sum>=(i)) {
				sum = sum + s[i]-48;
			}
			else {
				count = count + i-sum;
				sum = sum + i-sum+s[i]-48;
			}
	//		cout<<sum<<endl;
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
}
