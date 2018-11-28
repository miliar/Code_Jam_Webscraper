#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main(){
	// cout<<"Case #"<<k<<": INSOMNIA"<<endl;
	int n,t;
	string s;
	//2 for + to -, check it 
	int flips;
	int start;
	cin>>t;
	bool state;//false for -, true for +
	for (int k=1;k<=t;k++){
		cin>>s;
		n = s.size();
		flips = 0;
		start = n;
		for (int i=0;i<n;i++){
			if (s[i]=='+'){
				start = i;
				break;
			}
		}
		if (start!=0) flips++;
		state = true;//because in plus
		for (int i=start;i<n;i++){
			if(s[i]=='+'){
				//do nothing
				state = true;
			}
			else {
				if (state){
					flips+=2;
				}
				state = false;
			}
		}
		cout<<"Case #"<<k<<": "<<flips<<endl;
	}
	return 0;
}