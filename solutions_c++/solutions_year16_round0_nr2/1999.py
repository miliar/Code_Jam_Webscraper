#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	string s;
	for(int tc=1;tc<=t;tc++){
		cin>>s;
		int seg=0;
		for(int i=1;i<s.size();i++){
			if(s[i]!=s[i-1])seg++;
		}
		if(s.back()=='-')seg++;
		printf("Case #%i: %i\n",tc,seg);
	}
}
