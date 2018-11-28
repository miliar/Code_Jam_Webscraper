#include<iostream>
#include<string>

using namespace std;

int main(){
	int kases; cin>>kases;
	for(int kase = 1; kase <= kases; kase++){
		int res=0, cum=0, shyest;
		string s;
		cin>>shyest>>s;
		for(int i=0;i<=shyest;i++){
			if(s[i] != '0'){
				if(cum < i){
					res+= (i-cum);
					cum = i;
				}
			}
			cum += int(s[i]-'0');
		}
		cout<<"Case #"<<kase<<": "<<res<<endl;	
	}
}
