#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int caseno=0;
	int mm =0;
	while(t--){
		caseno++;
		int ans=0;
		string s;
		cin>>s;
		int l = s.length()-1;
		while(l>=0){
			if(s[l]=='-'){
				ans++;
				for(int i=0;i<l;i++)
					if(s[i]=='+')
						s[i]='-';
					else
						s[i]='+';
			}
			l--;
		}
		
		cout<<"Case #"<<caseno<<": "<<ans<<endl;
		
	}
	
	return 0;
}
