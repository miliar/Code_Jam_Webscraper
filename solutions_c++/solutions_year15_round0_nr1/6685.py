#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	int s_max;
	string val;
	int cnt = 0;
	for (int i = 0; i < t; i++) {
		cnt++;
		cin>>s_max;
		cin>>val;
		int ppl = 0;
		int need = 0;
		for (int j = 0;j<val.length();j++) {
			if (val[j]-48!= 0) {
				int temp = max(j-ppl,0);
				need += temp;
				ppl+= temp;
			}
			ppl+= val[j]-48;
		}
		cout<<"Case #"<<cnt<<": "<<need<<endl;
	}
	return 0;
}