#include<bits/stdc++.h>
 
using namespace std;
 
int main(){
 
 	//std::ios_base::sync_with_stdio(false);cin.tie(false);
	int t,i,j,k,l,x,flips;
	cin>>t;
	for(x=1;x<=t;x++){
		string s,ans; char last;
		cin>>s;
		ans.push_back(s[0]);
		last = ans[0];
		for(i=1;i<s.size();i++){
			if(int(s[i])>=int(last)){
				string temp;
				temp.push_back(s[i]);
				temp.append(ans);
				ans = temp;
				last= s[i];
			}else{
				ans.push_back(s[i]);
			}
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
	}
 
	return 0;
}