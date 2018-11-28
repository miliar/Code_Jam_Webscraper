#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int S[1100];

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin>>T;

	for(int t=1 ; t<=T ; t++) {
		string input;
		int ans=0, cnt=0, s_max;

		cin>>s_max>>input;
		for(int i=0 ; i<=s_max ; i++) S[i]=input[i]-'0';

		for(int i=0 ; i<=s_max ; i++) {
			ans += (i-cnt>0)?(i-cnt):0;
			cnt += S[i] + ((i-cnt>0)?(i-cnt):0);
		}				

		cout<<"Case #"<<t<<": ";
		cout<<ans<<"\n";
	}


	return 0;
}