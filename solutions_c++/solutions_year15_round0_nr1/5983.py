#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;
int T = 0;
int N = 0;
void solve(int len, string s) {
	ofstream outFile;
	outFile.open("result.txt",ios::app);
	int res = 0;
	int sum = 0;
	for(int i = 0; i <= len; i++) {
		sum += (s[i] - '0');
		if(s[i] == '0' && sum < i+1) {
			res += (i + 1 - sum);
			//cout<<res<<" ";
			sum += (i + 1 - sum);
		}
	}

	outFile<<"Case #"<<(N-T)<<": "<<res<<endl;
	outFile.close();
}

int main() {
	cin >>T;
	N = T;
	int len = 0;
	string s;
	while(T--) {
		cin>>len>>s;
		solve(len,s);
	}
}

