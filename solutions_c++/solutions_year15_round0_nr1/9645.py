#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, l = 1;
	cin>>t;

	while(t--){
		int n, sum, ans = 0;
		cin>>n;

		string s;
		cin>>s;

		sum = s[0] - '0';
		for(int i=1 ; i<n+1 ; i++){
			if(sum>=i){
				sum += s[i] - '0';
			} else {
				ans += i - sum;
				sum = i;
				sum += s[i] - '0';
			}
		}

		cout<<"Case #"<<l++<<": ";
		cout<<ans<<endl;
	}

	return 0;
}