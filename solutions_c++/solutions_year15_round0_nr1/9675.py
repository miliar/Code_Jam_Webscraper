#include<iostream>
#include<string>
using namespace std;

int main() {
	int t, n;
	string s = "";
	cin>>t;
	for(int testCase = 1; testCase <= t; ++testCase){
		cin>>n;
		cin>>s;
		int count = 0, ans = 0;
		for(int i=0;i<n+2;++i){
			int temp = (i > count)?(i-count):0;
			ans += temp;
			count += temp;
			count+=(s[i]-'0');
		}
		cout<<"Case #"<<testCase<<": "<<ans<<endl;
	}
	return 0;
}