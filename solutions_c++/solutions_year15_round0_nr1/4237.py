#include <iostream>

using namespace std;

int T,n;
string st;

int main(){
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		cin >> n >>st;
		int tot=st[0]-48;
		int ans=0;
		for (int i=1;i<st.length();i++){
			int now = st[i]-'0';
			if (now==0) continue;
			if (i>tot) {ans+=i-tot;tot=i;}
			tot+=now;
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
	return 0;
}
