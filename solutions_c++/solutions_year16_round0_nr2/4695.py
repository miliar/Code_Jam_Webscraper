#include<iostream>
using namespace std;
int main(){
	int t,T,ans,size;
	string s;
	bool statePlus;
	cin>>T;
	for(int t=1;t<=T;t++){
		ans=0;
		cin>>s;
		size = s.size();
		statePlus=s[0]=='+'?true:false;
		for(int i=1;i<size;i++){
			if(s[i]=='+' && statePlus==false){
				ans++;
				statePlus=true;
			}else if(s[i]=='-' && statePlus==true){
				ans++;
				statePlus=false;
			}
		}
		if(statePlus==false){
			ans++;
			statePlus=true;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
