#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int cases;
	cin>>cases;
	for (int c=0;c<cases;c++){
		cout<<"Case #"<<c+1<<": ";
		int flips = 0;
		string s;
		cin>>s;
		int state = -1;
		for (int i=0;i<s.size();i++){
			if (s[i] == '-'){
				if (state != 1){
					state = 1;
					flips++;
				}
			}
			else{
				if (state != 0){
					state = 0;
					flips++;
				}
			}
			if (i == s.size()-1){
				if (state == 1){
					flips++;
				}
			}
		}
		cout<<flips-1<<"\n";
	}
	return 0;
}