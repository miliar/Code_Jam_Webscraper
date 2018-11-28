#include <iostream>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main(int argc, char** argv) {
	int t,count=1,sol;
	string s;
	cin>>t;
	while(count<=t){
		cin>>s;
		cout<<"Case #"<<count<<": ";
		count++;
		sol=0;
		for(int i=1;i<s.length();i++){
			if(s[i-1]!=s[i]) sol++;
		}
		if(s[s.length()-1]=='-') sol++;
		cout<<sol<<endl;
	}
	return 0;
}
