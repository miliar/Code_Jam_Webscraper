#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

//100 * 1000 * 1000
int solve(string& s){
	for(int i=0;i<=1000;i++){
		int sum = i + s[0] - '0';
		for(int j=1;j<s.size();j++){
			if(sum < j)break;
			if(j == s.size()-1)return i;
			sum += s[j]-'0';
		}
	}
}

int main(void) {
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		int n;string s;
		cin >> n >> s;
		cout << "Case #" << i+1 << ": " << solve(s) << endl;
	}
	
	return 0;
}

