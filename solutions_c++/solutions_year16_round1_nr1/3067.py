#include<iostream>
using namespace std;

main(){
	
	int T;
	cin>>T;
	for(int t=0;t<T;t++){

		string s,s1;
		cin>>s;
		s1.push_back(s[0]);
		for(int i=1;i<s.size();i++){
			
			if(s1[0]>s[i]){
				s1.push_back(s[i]);
			}else{
				string t=s[i]+s1;
				//cout<<t;
				s1.clear();
				s1=t;
			}
		}
		cout<<"Case #"<<t+1<<": "<<s1<<"\n";
	}
}