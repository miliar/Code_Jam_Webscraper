#include <iostream>
using namespace std;
int TC, mlev;
string aud;
int main(){
	cin>>TC;
	for(int i=1;i<=TC;++i){		
		cin>>mlev>>aud;
		int cnt=0, ans=0;
		for(int j=0;j<aud.size();++j){
			if(aud[j]!='0'){
				if(j>cnt){ 
					ans+=j-cnt;
					cnt+=j-cnt; //add the audience we bring in
				}
				cnt+=aud[j]-'0';
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}