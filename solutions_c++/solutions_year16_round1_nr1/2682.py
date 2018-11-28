#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
	int testCase; cin>>testCase;
	for (int i=0; i<testCase; i++) {
		string input; cin>>input;
		string ans=string (1, input[0]);
		
		for (int j=1; j<input.size(); j++) 
			if (input[j]>=ans[0]) ans=input[j]+ans;
			else ans=ans+input[j];
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
