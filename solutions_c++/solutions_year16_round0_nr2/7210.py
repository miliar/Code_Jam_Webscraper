#include <iostream>
#include <string>

using namespace std;

int t;
string s;

int main() {
	// your code goes here
	
	cin >> t;
	
	for(int ii=1;ii<=t;ii++){
		cin >> s;
		int n = s.length();
		int count = 1;
		for(int i=1;i<n;i++){
			if(s.at(i)!=s.at(i-1))
				count++;
		}
		
		if(s.at(n-1)=='+') count--;
		//if(s.at(0)=='+') count++;
		
		cout << "Case #"<<ii<<": "<<count<<endl;
		
	}
	
	return 0;
}
