#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, t1=1, i, n;
	string s, s1;
	char c;
	bool flag=true;
	int flips;
	cin>>t;
	while(t--){
		flips=0;
		cin>>s;
		n=s.length();
		c=s.at(0);
		for(i=1;i<n;i++){
			if(c!=s.at(i)){
				flips++;
				c=s.at(i);
			}
		}
		if(s.at(n-1)=='+'){
			cout<<"Case #"<<t1<<": "<<flips<<"\n";
			t1++;
		}
		else{
			cout<<"Case #"<<t1<<": "<<flips+1<<"\n";
			t1++;			
		}
	}
	return 0;
}
