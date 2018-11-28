#include<bits/stdc++.h>
 
using namespace std;
 
int main(){
 
 	//std::ios_base::sync_with_stdio(false);cin.tie(false);
	int t,i,j,k,l,x,flips;
	cin>>t;
	for(x=1;x<=t;x++){
		string s; char last;
		cin>>s;
		flips=0;
		last = s[0];
		if(s[0]=='-')
			s[0]='+';
		else
			s[0]='-';
		for(i=1;i<s.size();i++){
			if(s[i]!=last){
				flips++;
				last = s[i];
			}
			if(s[i]=='-')
				s[i]='+';
			else
				s[i]='-';
		}
		if(last=='-')
			flips++;
		k=flips;
		flips=0;
		last = s[0];
		// for(i=1;i<s.size();i++){
		// 	if(s[i]!=last){
		// 		flips++;
		// 		last = s[i];
		// 	}
		// }
		// if(last=='-')
		// 	flips++;
		// l=flips;
		// cout<<"k:"<<k<<" l:"<<l<<"\n";
		cout<<"Case #"<<x<<": "<<k<<"\n";
	}
 
	return 0;
}
