#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;
string s;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	long int t;
	scanf("%ld",&t);
	for(long int c=1;c<=t;c++){
		char pss;
		long long flip=0;
		string s;
		cin>>s;
		//cout<<s<<endl;
		pss=s[0];
		if(s.size()==1){
		//	cout<<"first"<<endl;
			if(s[0]=='-') flip++;
			cout<<"Case #"<<c<<": "<<flip<<endl;
			continue;
		}
		//cout<<"Inside loop"<<endl;
		for(int i =1;i<s.size();i++){
			//cout<<"prev pss :"<<pss<<endl;
			if(s[i]==pss){
				//cout<< s[i] <<" same as pss"<<endl;
				if(i==s.size()-1){
				//	cout<<"last el"<<endl;
					if(s[i]=='-') flip++;
					break;
				}
				//i++;
			}
			else{
				//cout<<s[i]<<" diff from pss"<<endl;
				pss=s[i];
				if(i == s.size()-1){
					//cout<<"last el"<<endl;
					if(s[i]=='-') flip+=2;
					else flip++;
					break;
				}
				flip++;
			}
		}
		cout<<"Case #"<<c<<": "<<flip<<endl;


	}
return 0;
}
