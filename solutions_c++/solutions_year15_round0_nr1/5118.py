#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int t=1; t<=T; t++){
		int N;
		cin>>N;
		string S;
		cin>>S;
		int ans = 0, cur = 0;
		for(int i=0; i<=N; i++){
			if(cur < i){
				ans += i-cur;
				cur = i;
			}
			cur += int(S[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
