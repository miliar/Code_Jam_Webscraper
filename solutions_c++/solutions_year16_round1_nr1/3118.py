#include <bits/stdc++.h>

using namespace std;
int main(){
	string s;
	int t;
	deque<char> out;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>s;
		for(int j=0;j<s.size();j++){
			if(j==0)
				out.push_back(s[j]);
			else{
				if(s[j]>=out[0]){
					out.push_front(s[j]);
				}
				else{
					out.push_back(s[j]);
				}
			}
		}
		printf("Case #%d: ",i );
		for(int j=0;j<out.size();j++){
			cout<<out[j];
		}
		cout<<endl;
		out.clear();
	}

	return 0;
}