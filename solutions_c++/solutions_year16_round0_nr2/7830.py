#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for (int k = 1; k<=t; k++){
		string s;
		cin>>s;
		int count = 0;
		for (int i = 1; i<s.size(); i++){
			if (s[i] == s[i-1])
				continue;
			count++;
		}
		if (s[s.size()-1] == '-')
			++count;
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}