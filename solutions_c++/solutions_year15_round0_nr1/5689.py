#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main () {
	int t;
	cin >> t;
	for(int k=1;k<=t;k++){
		int smax,ans,total;
		string s;
		cin >> smax >> s;
		ans=total=0;
		for(int i=0;i<s.size();i++){
			if(i>total&&s[i]!='0'){
				ans+=i-total;
				total+=(i-total);
			}
			total+=s[i]-'0';
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;	
	}
	return 0;
}
