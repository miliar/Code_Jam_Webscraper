#include <iostream>
#include <string>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int t, L=1;
	cin>>t;

	while(t--){
		string s, temp;
		cin>>s;

		int l = s.size();
		char last = '@';
	
		for(int i=0 ; i<l ; i++)
			if(s[i] != last)
				temp.push_back(s[i]), last = s[i];
		
		int ans = 0;

		for(int i=0 ; i<temp.size() ; i++)
			if(temp[i] == '-')
				ans = i + 1;

		cout<<"Case #"<<L++<<": ";
		cout<<ans<<"\n";
	}

	return 0;
}