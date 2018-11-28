#include<iostream>
#include<cstring>

using namespace std;

int main(){
	int t;
	int j;

	cin>>t;


	for(j=1;j<=t;j++){
		string s;
		cin>>s;
		//cout<<s<<endl;
		s+='+';
		int ps;
		if(s[0]=='+'){
			ps=1;
		}else{
			ps=-1;
		}
		int i;
		int net=0;
		for(i=1;i<s.size();i++){
			if(s[i]=='+'&&ps==-1){
				net++;
				ps=1;
			}
			if(s[i]=='-'&&ps==1){
				net++;
				ps=-1;
			}
		}

		cout<<"Case #"<<j<<": "<<net<<endl;



	}


	return 0;
}