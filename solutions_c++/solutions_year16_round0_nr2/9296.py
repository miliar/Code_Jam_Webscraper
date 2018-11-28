#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string s;
	cin>>t;
	for(int l=1;l<=t;l++){
		vector<char> v;
		cin>>s;
		v.push_back(s[0]);
		for(int i=1;i<s.length();i++){
			if(s[i]!=v[v.size()-1]){
				v.push_back(s[i]);
			}
		}
		int u=v.size();
		if(v[v.size()-1]=='-'){
			printf("Case #%d: %d\n",l,u);
		}else{
			printf("Case #%d: %d\n",l,u-1);
		}
		
	}	
	return 0;
}