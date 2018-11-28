#include "bits/stdc++.h"
using namespace std;

int main(void){
	int i, t; cin>>t;
	for(i = 1; i <= t; i++){
		cout<<"Case #"<<i<<": ";
		string s; cin>>s;
		s = s+"+";
		int l = s.size();
		int j;
		int count = 0;
		for(j = 1; j < l; j++){
			if(s[j] != s[j-1]) count++;
		}
		cout<<count<<endl;
	}
}
