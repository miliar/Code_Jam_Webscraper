#include <bits/stdc++.h>

using namespace std;

int testcase = 0;

fstream myfile ("abc.txt");

void solve(){
	testcase++;
	
	int smax;
	string s;
	cin>>smax;
	cin>>s;
	int cum[smax+1];
	int offset = 0;
	for(int i = 0; i<smax+1; i++){
		if(i==0){
			cum[i] = (s[i]-'0');
			offset += max(i - cum[i],0);
		}else{
			cum[i] = cum[i-1] + (s[i]-'0');
			if(cum[i-1]+offset<i) offset += i - cum[i-1] - offset;
		}
	}
	myfile<<"Case #"<<testcase<<": "<<offset<<endl;
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}