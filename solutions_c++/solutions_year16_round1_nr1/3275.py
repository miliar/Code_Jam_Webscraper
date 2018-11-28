#include <iostream>
using namespace std;

int main() {
	// your code goes here


	int t;
	cin>>t;
	int ii=0;

	while(ii++<t){
		string s,ans="";
		cin>>s;

		if(s.size()<2){
			cout<<"Case #"<<ii<<": "<<s<<endl;
			return 0;
		}
		ans = s[0];
		for(int i=1;i<s.size();i++){
			if(ans[0]<=s[i]){
				ans = s[i] + ans;
			}else{
				ans = ans+ s[i] ;
			}
		}

		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}



	return 0;
}
