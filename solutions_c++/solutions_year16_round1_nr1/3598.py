#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>
using namespace std;

bool comp(string a, string b) {
	for(int i = 0; i < a.size(); i++) {
		if(a[i] != b[i])
			return a[i] < b[i];
	}
	return true;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	string s,res, temp;
	for(int k = 1; k <= T; k++) {
		cin>>s;
		res = "";
		for(int i = 0; i < s.size(); i++) {
			if (comp(res + s[i] , s[i] + res)) {
				res =  s[i] + res;
			}
			else {
				res = res + s[i];
			}
		}
		cout<<"Case #"<<k<<": "<<res<<endl;
	}

	return 0;
}