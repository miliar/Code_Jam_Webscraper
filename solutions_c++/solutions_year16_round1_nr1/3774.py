#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define mod 1000000007
int main(){
	int t;
	cin>>t;
	for (int k = 1; k<=t; k++){
		string s,s1,s2,ans;
		cin>>s;
		ans = s[0];
		for (int i = 1; i<s.size(); i++){
			if (s[i]>=ans[0]){
				s1 = s[i];
				s1 += ans;
				ans = s1;
			}else{
				ans += s[i];
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}