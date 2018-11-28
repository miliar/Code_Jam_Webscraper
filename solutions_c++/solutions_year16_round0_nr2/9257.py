#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		string s;
		cin>>s;
		int l=s.length();
		int c;
		if(s[0]=='-')	c=1;
		else c=0;
		int i=0;
		while(s[i]=='-')	i++;
		int ch=0;
		while(i<l-1){
			if(s[i+1]!=s[i]) ch++;
			i++;
		}
		if(ch%2) ch++;
		c=c+ch;
		cout<<c<<endl;
		
		
		
		
		
		
		
		
		
	}
	return 0;
}