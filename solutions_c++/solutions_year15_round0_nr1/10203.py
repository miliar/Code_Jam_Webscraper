#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T,c=0;
	cin>>T;
	while(T--){
		c++;
		int smax,totalclaps=0,ans=0;
		cin>>smax;
		string s;
		cin>>s;
		totalclaps = s[0] - '0';
		for(int i=1;i<=smax;i++){
			int x = s[i] - '0';
			if(totalclaps >= i){
				totalclaps += x;
			}
			else{
				int newpeople = i - totalclaps;
				ans += newpeople;
				totalclaps +=  newpeople + x;
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
