#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int end(string str){
	int re=0;
	for(int i=0;i<str.size();i++){
		if(str[i]=='-')re=i+1;
	}
	return re;
}

int main(){
	int n;
	cin>>n;
	for(int l=1;l<=n;l++){
		string str;
		cin>>str;
		int e=end(str);
		int ans=0;
		while(e!=0){
			ans++;
			if(str[0]=='-'){
				string tmp_str=str.substr(0,e);
				reverse(tmp_str.begin(),tmp_str.end());
				for(int i=0;i<tmp_str.size();i++){
					if(tmp_str[i]=='-')tmp_str[i]='+';
					else tmp_str[i]='-';
				}
				str=tmp_str;
			}
			else{
				int c=0;
				while(str[c]=='+')str[c++]='-';
			}
			e=end(str);
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
}
