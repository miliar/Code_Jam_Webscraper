#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int h=0;h<t;h++){
		long long ans=0;
		long long mx=0;
		string s;
		cin>>mx>>s;
		long long cnt = s[0]-'0';
		//cout<<cnt<<endl;
		for(int i=1;i<mx+1;i++){
			if(cnt >= i && s[i] !='0'){
				cnt += (s[i]-'0');
			}
			else {
				if(s[i]!='0'){
					long long temp = i-cnt;
					ans += temp;
					cnt += temp + (s[i]-'0');
				}
			}
			//cout<<cnt<<" "<<ans<<endl;
		}
		cout<<"Case #"<<(h+1)<<": "<<ans<<endl;
	}
}
