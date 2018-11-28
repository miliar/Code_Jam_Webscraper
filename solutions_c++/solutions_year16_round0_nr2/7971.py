#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int t;
	cin>>t;
	string s;
	for(int i=1;i<=t;i++){
		cin>>s;
		int cnt=0,k;
		int j = s.length()-1;
		while(s[j]!='-' && j>=0){
			cnt++;
			j--;
		}
		s = s.substr(0,s.length()-cnt);
		cnt = 0,k=0;
		string x;
		for(int j=0;j<s.length();j++){
			if(j==0){
				x = x + s[j];
				k++;
			}
			else if(x[k-1] != s[j])
			{
				x = x + s[j];
				k++;
			}
		}
		cout<<"Case #"<<i<<": "<<x.length()<<"\n";
	}
	return 0;
}