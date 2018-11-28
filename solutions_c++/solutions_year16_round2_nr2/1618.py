#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool check(string s, string s2){
	if(s.length() != s2.length()) return false;
	for(int i = 0; i < s.length(); ++i){
		if(s[i] != s2[i] && s[i] != '?') return false;
	}
	return true;
}
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	int t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		string a,b; cin>>a>>b;
		int mini = 1000000000;
		string solia, solib;
		for(int i = 0 ; i < 1000; ++i){
			stringstream ss1, ss2, ss3, ss4; ss1<<i; ss2<<"0"<<i; ss3<<"00"<<i; ss4<<"000"<<i;
			string s1 = ss1.str(), s2 = ss2.str(), s3 = ss3.str(), s4 = ss4.str();
			if(check(a, s1)||check(a, s2)||check(a, s3)||check(a, s4)){

				string soliaa;
				if(check(a, s1)) soliaa = s1;
				if(check(a, s2)) soliaa = s2;
				if(check(a, s3)) soliaa = s3;
				if(check(a, s4)) soliaa = s4;
				//cout<<i<<soliaa<<endl;
				for(int j = 0; j < 1000; ++j){
					stringstream ss1, ss2, ss3, ss4; ss1<<j; ss2<<"0"<<j; ss3<<"00"<<j; ss4<<"000"<<i;
					string s1 = ss1.str(), s2 = ss2.str(), s3 = ss3.str(), s4 = ss4.str();

				
					if((check(b, s1)||check(b, s2)||check(b, s3)||check(b, s4)) && abs(i - j) < mini){
						//cout<<i<<" "<<j<<" "<<b<<" "<<check(b, j)<<" "<<abs(i - j)<<endl;
						string solibb;
						if(check(b, s1)) solibb = s1;
						if(check(b, s2)) solibb = s2;
						if(check(b, s3)) solibb = s3;
						if(check(b, s4)) solibb = s4;
						solia = soliaa; solib = solibb; mini = abs(i - j);
					}
				}	
			}
		}
		cout<<"Case #"<<(i + 1)<<": "<<solia<<" "<<solib<<"\n";
	}
	return 0;
}
