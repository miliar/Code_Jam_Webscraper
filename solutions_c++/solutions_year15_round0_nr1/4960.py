#include<iostream>

using namespace std;

int main() {
	int t,smax;
	char s[1002];
	
	cin>>t;
	for(int ti = 1; ti <= t ; ti++) {
		cin>>smax;
		cin>>s;
		
		int included = 0;
		int totalStoodUp = s[0] - '0';
		for(int i = 1; i<= smax; i++) {
			if(totalStoodUp < i) {
				included += i - totalStoodUp;
				totalStoodUp = i + (s[i] - '0');
			}
			else {
				totalStoodUp += (s[i] - '0');
			}
		}
		
		cout<<"Case #"<<ti<<": "<<included<<endl;
	}

}