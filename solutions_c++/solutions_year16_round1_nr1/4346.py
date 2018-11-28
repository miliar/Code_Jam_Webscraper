#include <iostream>
using namespace std;

int T;
string S;

void solve()
{

	string ret(1, S[0]);
	for(int i=1;i<S.length();++i){
		if(S[i]>=ret[0]){
			string temp (1, S[i]);
			ret = temp + ret;

			
		}
		else{
			ret = ret + S[i];
		}
	}
	cout<<ret;
}

int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		cin>>S;
		cout<<"Case #"<<xx<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}
