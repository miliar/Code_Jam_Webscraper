#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string s;
		cin>>s;
		if(s.size()==1){
			cout<<"Case #"<<i+1<<": "<<s[0]<<endl;
		}else if(s.size()==2){
			sort(s.begin(),s.end());
			reverse(s.begin(),s.end());
			cout<<"Case #"<<i+1<<": "<<s<<endl;
		}else{
			vector<char> ans;
			ans.push_back(s[0]);
			char actual=s[0];
			for(int i=1;i<s.size();i++){
				if(s[i]>=actual){
					ans.insert(ans.begin(),s[i]);
					actual=s[i];
				}else{
					ans.push_back(s[i]);
				}
			}
			cout<<"Case #"<<i+1<<": ";
			for(int i=0;i<ans.size();i++)cout<<ans[i];
			puts("");
		}
	}
	return 0;
}


