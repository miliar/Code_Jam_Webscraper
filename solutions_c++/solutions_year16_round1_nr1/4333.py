#include<iostream>
#include<cstring>
#include<string>
using namespace std;
int main(void){
	int t,i,j=1;
	string s,ns,ns1;
	cin>>t;
	while(t--){
		cin>>s;
		for(i=0;i<s.length();i++){
			if(i==0)ns.push_back(s[i]);
			else if((int)s[i]-'0'>=(int)ns[0]-'0'){
				ns.insert(0,1,s[i]);
			}else{
				ns.push_back(s[i]);
				//cout<<"2"<<ns<<endl;
			}
		}
		cout<<"Case #"<<j<<": "<<ns<<endl;
		j++;
		ns.clear();
	}
	return 0;
}