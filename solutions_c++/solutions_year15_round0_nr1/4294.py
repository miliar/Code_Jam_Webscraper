#include<iostream>

using namespace std;

int main() {
	int t,i,j,k,mx,ans,cur,temp;
	string s;
	cin >> t;
	for(k=1;k<=t;k++) {
		cin >> mx;
		cur=0;
		ans=0;
		cin >> s;
		cur=s[0]-'0';
		for(i=1;i<=mx;i++) {
			if(cur < i){
				temp = i-cur;
				ans += temp;
				cur += (temp+s[i]-'0');
			}
			else {
				cur += (s[i]-'0');
			}
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}
