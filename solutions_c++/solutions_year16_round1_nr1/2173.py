#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	int t;
	cin>>t;
	string s,sc;
	for(int i=1;i<=t;i++){
		cin>>s;
		string x;
		x = x + s[0];
		for(int i=1;i<s.size();i++){
			if(s[i]>=x[0])
			{
				x = s[i] + x;
			}
			else{
				x = x + s[i];
			}
		}
		cout<<"Case #"<<i<<": "<<x<<endl;
	}
	return 0;
}