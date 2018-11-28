#include <iostream>
#include <string>
using namespace std;

int main() {
	int t,smax,T;
	cin>>t;
	T= t;
	string s;
	while(t--){
		cin>>smax;
		cin>>s;
		int i = 0, curr = 0, c = 0;
		while(i <= smax){
			curr = curr + (s[i] - 48);
			i++;
		//	cout<<curr<<" "<<i<<endl;
			if(curr < i){
				c = c + (i - curr);
				curr = curr + (i - curr);
			}
		}
		cout<<"Case #"<<T-t<<": "<<c<<endl;
	}
	return 0;
}
